import tkinter as tk
import tkinter.ttk as ttk


class Teste(tk.Frame):
    def __init__(self, master):
        self.containerV1 = tk.Frame(master,
                                    bd=5)

        self.containerV2 = tk.Frame(master,
                                    bd=5)
        self.containerV1.pack(
            fill='both', side="left",
            expand=1, padx=3, pady=3)
        self.containerV2.pack(
            fill='both', side="left",
            expand=1, padx=3, pady=3)

        # INSERÇÃO E PESQUISA
        self.containerV3 = tk.Frame(self.containerV1)
        self.containerV3.pack(fill='both', expand=1, padx=3, pady=3)

        tk.Label(self.containerV3, text="ID:").grid(row=0, column=0)
        self.id = tk.Entry(self.containerV3, state="readonly")
        self.id.grid(row=0, column=1)

        tk.Label(self.containerV3, text="NOME*:").grid(row=1, column=0)
        self.nome = tk.Entry(self.containerV3)
        self.nome.grid(row=1, column=1)

        tk.Label(self.containerV3, text="IDADE:").grid(row=2, column=0)
        self.idade = tk.Entry(self.containerV3)
        self.idade.grid(row=2, column=1)

        tk.Label(self.containerV3, text="CPF*:").grid(row=3, column=0)
        self.cpf = tk.Entry(self.containerV3)
        self.cpf.grid(row=3, column=1)

        tk.Label(self.containerV3, text="E-MAIL*:").grid(row=4, column=0)
        self.email = tk.Entry(self.containerV3)
        self.email.grid(row=4, column=1)

        tk.Label(self.containerV3, text="FONE:").grid(row=5, column=0)
        self.fone = tk.Entry(self.containerV3)
        self.fone.grid(row=5, column=1)

        tk.Label(self.containerV3, text="CIDADE:").grid(row=6, column=0)
        self.cidade = tk.Entry(self.containerV3)
        self.cidade.grid(row=6, column=1)

        tk.Label(self.containerV3, text="UF:").grid(row=7, column=0)
        self.uf = tk.Entry(self.containerV3)
        self.uf.grid(row=7, column=1)

        self.containerV4 = tk.Frame(self.containerV1)
        self.containerV4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(
            self.containerV4,
            text="INSERIR"
        )
        self.btn_inserir.pack(side="left", expand=1, fill="both")

        self.btn_pesquisar = tk.Button(self.containerV4,
                                    text="PESQUISAR"
                                    )
        self.btn_pesquisar.pack(side="left", expand=1, fill="both")

        # VISUALIZAR REGISTROS
        self.containerV5 = tk.Frame(self.containerV2)
        self.containerV5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.containerV5, orient="vertical")
        barraH = tk.Scrollbar(self.containerV5, orient="horizontal")
        self.lista_clientes = tk.Listbox(
            self.containerV5,
            width=20,
            yscrollcommand=barraV.set,
            xscrollcommand=barraH.set,
            selectmode="SINGLE"
        )
        barraV.config(command=self.lista_clientes.yview)
        barraV.pack(side="right", fill='y')

        self.containerV6 = tk.Frame(self.containerV2)
        self.containerV6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='x')

        self.lista_clientes.pack(fill='x')
        tk.Button(
            self.containerV6,
            text="DELETAR"
        ).pack(side="left", expand=1, fill="both")
        tk.Button(
            self.containerV6,
            text="EDITAR"
        ).pack(side="left", expand=1, fill="both")


if __name__ == "__main__":
    app = tk.Tk()
    Teste(app)
    app.mainloop()
