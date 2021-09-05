import tkinter as tk
import tkinter.ttk as ttk


class TelaPrincipalCliente(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        master.title("MENU PRINCIPAL")

        self.container1 = tk.Frame(master)
        self.container1.pack(fill="both", expand=1)

        self.menu = tk.Menu(self.container1, borderwidth=1)
        self.prog = tk.Menu(self.menu, tearoff=0)
        self.prog.add_command(label="Fechar", command=self.fechar)
        self.menu.add_cascade(label="Programa", menu=self.prog)

        master.config(menu=self.menu)

        self.abas = ttk.Notebook(self.container1)
        self.abas.pack(fill="both", expand=1, padx=3, pady=3)

        self.painel_contrato = tk.Frame(self.abas)
        self.painel_pagar = tk.Frame(self.abas)

        self.painel_contrato.pack(fill="both", expand=1)
        self.painel_pagar.pack(fill="both", expand=1)

        self.abas.add(self.painel_contrato, text="NOVO CONTRATO")
        self.abas.add(self.painel_pagar, text="PAGAR CONTRATO")

        tk.Label(self.container1,
                 text="Usuário: Fulano da Silva",
                 font="Verdana").pack(side="left", fill="both", padx=3, pady=3)

        tk.Button(self.container1, text="Logout",
                  command=self.fechar).pack(side="right",
                                            fill="both",
                                            padx=3,
                                            pady=3)

        # Contratos

        self.containerC1 = tk.Frame(self.painel_contrato, bd=5)

        self.containerC2 = tk.Frame(self.painel_pagar, bd=5)
        self.containerC1.pack(fill='both',
                              side="left",
                              expand=1,
                              padx=3,
                              pady=3)
        self.containerC2.pack(fill='both',
                              side="left",
                              expand=1,
                              padx=3,
                              pady=3)

        # INSERÇÃO
        self.container3 = tk.Frame(self.containerC1)
        self.container3.pack(fill='both', expand=1, padx=3, pady=3)

        tk.Label(self.container3, text="VEÍCULO:").grid(row=0, column=0)
        self.veiculo = ttk.Combobox(self.container3)
        self.veiculo.grid(row=0, column=1)

        tk.Label(self.container3, text="PERÍODO:").grid(rowspan=2,
                                                        row=1,
                                                        column=0)
        self.containerPeriodo = tk.Frame(self.container3)
        self.containerPeriodo.grid(row=1, column=1)
        self.inicio = tk.Entry(self.containerPeriodo, width=10)
        self.fim = tk.Entry(self.containerPeriodo, width=10)

        tk.Label(self.containerPeriodo, text="De").grid(column=0, row=0)
        self.inicio.grid(column=1, row=0)
        tk.Label(self.containerPeriodo, text="Até").grid(column=0, row=1)
        self.fim.grid(column=1, row=1)

        tk.Label(self.container3, text="COMBUSTÍVEL:").grid(row=2, column=0)
        self.combustivel = ttk.Combobox(self.container3)
        self.combustivel.grid(row=2, column=1)

        self.container4 = tk.Frame(self.containerC1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4, text="CRIAR CONTRATO")
        self.btn_inserir.pack(side="left", expand=1, fill="both")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.containerC2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_clientes = tk.Listbox(self.container5,
                                         width=20,
                                         yscrollcommand=barraV.set,
                                         xscrollcommand=barraH.set,
                                         selectmode="SINGLE")
        barraV.config(command=self.lista_clientes.yview)
        barraV.pack(side="right", fill='y')

        self.container6 = tk.Frame(self.containerC2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='x')

        self.lista_clientes.pack(fill='x')
        tk.Button(self.container6, text="PAGAR CONTRATO").pack(expand=1,
                                                               fill="both")

    def fechar(self):
        self.master.destroy()

    def retbutton(self):
        print(self.master.geometry())
        return 3


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("290x330")
    TelaPrincipalCliente(app)
    app.mainloop()
