import datetime
import tkinter as tk
import tkinter.ttk as ttk

DATA_BASE = datetime.date.today()


class TelaPrincipalCliente(tk.Frame):
    def __init__(self, master):
        global DATA_BASE
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

        self.abas = ttk.Notebook(self.container1, height=17)
        self.abas.pack(fill="both", expand=1, padx=3, pady=3)

        self.painel_contrato = tk.Frame(self.abas)
        self.painel_pagar = tk.Frame(self.abas)

        self.painel_contrato.pack(fill="both", expand=1)
        self.painel_pagar.pack(fill="both", expand=1)

        self.abas.add(self.painel_contrato, text="NOVO CONTRATO")
        self.abas.add(self.painel_pagar, text="PAGAR CONTRATO")

        tk.Label(self.container1,
                 text="Usuário: Fulano da Silva",
                 font="Default 10").pack(side="left",
                                         fill="both",
                                         padx=3,
                                         pady=3)

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

        tk.Label(self.container3, text="VEÍCULO:").grid(row=0,
                                                        column=0,
                                                        sticky="w")
        self.veiculo = ttk.Combobox(self.container3, width=32)
        self.veiculo.grid(row=1, column=0, padx=3, pady=3)

        self.filtro = tk.Button(self.container3, text="Filtro")
        self.filtro.grid(row=0, column=0, sticky="e")

        tk.Label(self.container3, text="PERÍODO:").grid(row=2,
                                                        column=0,
                                                        padx=3,
                                                        pady=3,
                                                        sticky="w")
        self.containerPeriodo = tk.Frame(self.container3)
        self.containerPeriodo.grid(row=3, column=0, sticky="w")
        self.inicio = DateEntry(self.containerPeriodo,
                                DATA_BASE.strftime("%d/%m/%Y"),
                                width=10)
        DATA_BASE += datetime.timedelta(days=1)
        self.fim = DateEntry(self.containerPeriodo,
                             DATA_BASE.strftime("%d/%m/%Y"),
                             width=10)

        tk.Label(self.containerPeriodo, text="Início:").grid(column=0,
                                                             row=0,
                                                             padx=(5, 2))
        self.inicio.grid(column=1, row=0)
        tk.Label(self.containerPeriodo, text="Fim:").grid(column=2,
                                                          row=0,
                                                          padx=(5, 2))
        self.fim.grid(column=3, row=0)

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
                                         height=7,
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


class DateEntry(tk.Entry):
    def __init__(self, mst, data_base=DATA_BASE, **kwargs):
        tk.Entry.__init__(self, master=mst, **kwargs)
        self.data_base = data_base

        self.bind("<KeyPress>", self.__inserir)
        self.bind("<KeyRelease>", self.__inserir)
        self.bind("<FocusIn>", self.__cursor)
        self.bind("<ButtonRelease>", self.__cursor)
        self.cursorpos = 0

    def __cursor(self, e):
        self.icursor(self.cursorpos)

    def __inserir(self, e):
        if e.keysym in "0123456789":
            if len(self.get()) == 2:
                if self.get()[:2] > "31":
                    self.delete(0, tk.END)
                    self.insert(tk.END, "31")
                elif self.get()[:2] == "00":
                    self.delete(0, tk.END)
                    self.insert(0, "01")
                self.insert(tk.END, "/")

            elif len(self.get()) == 5:
                if self.get()[3:5] > "12":
                    self.delete(3, tk.END)
                    self.insert(tk.END, "12")
                elif self.get()[3:5] in ("04", "06", "09",
                                         "11") and self.get()[:2] == "31":
                    self.delete(1)
                    self.insert(1, "0")
                elif self.get()[3:5] == "02":
                    if self.get()[:2] > "29":
                        self.delete(0, 2)
                        self.insert(0, "29")
                elif self.get()[3:5] == "00":
                    self.delete(3, tk.END)
                    self.insert(tk.END, "01")

                self.insert(tk.END, "/")

            elif len(self.get()) >= 10:
                if self.get()[6:10] <= self.data_base[6:10]:
                    self.delete(6, tk.END)
                    self.insert(tk.END, self.data_base[6:10])

                    if self.get()[3:5] <= self.data_base[3:5]:
                        self.delete(3, 5)
                        self.insert(3, self.data_base[3:5])

                        if self.get()[:2] <= self.data_base[:2]:
                            self.delete(0, 2)
                            self.insert(0, self.data_base[:2])
                if self.get()[3:5] == "02":
                    if DateEntry.ehbissexto(int(self.get()[6:10])):
                        dm = "29"
                    else:
                        dm = "28"

                    if self.get()[:2] > dm:
                        self.delete(0, 2)
                        self.insert(0, dm)

                self.delete(10, tk.END)
            self.cursorpos = self.index(tk.INSERT)
        elif e.keysym == "BackSpace":
            self.delete(tk.END)
            self.cursorpos = self.index(tk.INSERT)
        elif e.keysym in ("Tab", "ISO_Left_Tab"):
            self.select_clear()
        else:
            return "break"

    def ehbissexto(ano):
        return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("310x260")
    TelaPrincipalCliente(app)
    app.mainloop()
