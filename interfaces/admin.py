import tkinter as tk
import tkinter.ttk as ttk


class TelaPrincipalAdmin(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        master.title("MENU PRINCIPAL")

        self.container1 = tk.Frame(master)
        self.container1.pack(fill="both", expand=1)

        self.menu = tk.Menu(self.container1, borderwidth=1)
        self.prog = tk.Menu(self.menu, tearoff=0)
        self.prog.add_command(label="Preferências", command=self.pref)
        self.prog.add_command(label="Fechar", command=self.fechar)
        self.menu.add_cascade(label="Programa", menu=self.prog)

        master.config(menu=self.menu)

        self.abas = ttk.Notebook(self.container1)
        self.abas.pack(fill="both", expand=1, padx=3, pady=3)

        self.painel_veiculo = tk.Frame(self.abas)
        self.painel_cliente = tk.Frame(self.abas)
        self.painel_contrato = tk.Frame(self.abas)
        self.painel_manutencao = tk.Frame(self.abas)

        self.painel_veiculo.pack(fill="both", expand=1)
        self.painel_cliente.pack(fill="both", expand=1)
        self.painel_contrato.pack(fill="both", expand=1)
        self.painel_manutencao.pack(fill="both", expand=1)

        self.abas.add(self.painel_veiculo, text="VEÍCULOS")
        self.abas.add(self.painel_cliente, text="CLIENTES")
        self.abas.add(self.painel_contrato, text="CONTRATOS")
        self.abas.add(self.painel_manutencao, text="MANUTENÇÕES")

        tk.Label(self.container1,
                 text="Admin: Fulano da Silva",
                 font="Verdana").pack(side="left", fill="both", padx=3, pady=3)

        tk.Button(self.container1, text="Logout",
                  command=self.fechar).pack(side="right",
                                            fill="both",
                                            padx=3,
                                            pady=3)

        # Veiculos
        self.veiculo = VeiculoFrame(self.painel_veiculo)
        # Clientes
        self.cliente = ClienteFrame(self.painel_cliente)
        # Contratos
        self.contrato = ContratoFrame(self.painel_contrato)
        # Manutenções
        self.manutencao = ManutencaoFrame(self.painel_manutencao)

    def fechar(self):
        self.master.destroy()

    def pref(self):
        print(self.master.geometry())

    def retbutton(self):
        print(self.master.geometry())
        return 3


class VeiculoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.container1 = tk.Frame(self.master, bd=5)

        self.container2 = tk.Frame(self.master, bd=5)
        self.container1.pack(fill='both',
                             side="left",
                             expand=1,
                             padx=3,
                             pady=3)
        self.container2.pack(fill='both',
                             side="left",
                             expand=1,
                             padx=3,
                             pady=3)

        # INSERÇÃO E PESQUISA
        self.container3 = tk.Frame(self.container1)
        self.container3.pack(fill='x', expand=1, padx=3, pady=3)

        tk.Label(self.container3, text="ID:").grid(row=0, column=0)
        self.id = tk.Entry(self.container3, state="readonly")
        self.id.grid(row=0, column=1)

        tk.Label(self.container3, text="PLACA:").grid(row=1, column=0)
        self.nome = tk.Entry(self.container3)
        self.nome.grid(row=1, column=1)

        tk.Label(self.container3, text="MARCA:").grid(row=2, column=0)
        self.idade = ttk.Combobox(self.container3)
        self.idade.grid(row=2, column=1)

        tk.Label(self.container3, text="MODELO:").grid(row=3, column=0)
        self.cpf = tk.Entry(self.container3)
        self.cpf.grid(row=3, column=1)

        tk.Label(self.container3, text="COR:").grid(row=4, column=0)
        self.email = tk.Entry(self.container3)
        self.email.grid(row=4, column=1)

        tk.Label(self.container3, text="DESCRIÇÃO:").grid(row=5, column=0)
        self.fone = tk.Entry(self.container3)
        self.fone.grid(row=5, column=1)

        tk.Label(self.container3, text="ANO:").grid(row=6, column=0)
        self.cidade = tk.Entry(self.container3)
        self.cidade.grid(row=6, column=1)

        tk.Label(self.container3, text="STATUS:").grid(row=7, column=0)
        self.uf = tk.Entry(self.container3)
        self.uf.grid(row=7, column=1)

        tk.Label(self.container3, text="ID MANUTENÇÃO:").grid(row=8, column=0)
        self.uf = tk.Entry(self.container3)
        self.uf.grid(row=8, column=1)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='x', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4, text="INSERIR", height=2)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       height=2)
        self.btn_pesquisar.pack(side="left", expand=1, fill="x")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_clientes = tk.Listbox(self.container5,
                                         width=30,
                                         yscrollcommand=barraV.set,
                                         xscrollcommand=barraH.set,
                                         selectmode="SINGLE")
        barraV.config(command=self.lista_clientes.yview)
        barraV.pack(side="right", fill='both')

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='both')

        self.lista_clientes.pack(fill='both', expand=1)
        tk.Button(
            self.container6,
            text="DELETAR",
            height=2,
        ).pack(side="left", expand=1, fill="x")
        tk.Button(
            self.container6,
            text="EDITAR",
            height=2,
        ).pack(side="left", expand=1, fill="x")


class ClienteFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.container1 = tk.Frame(self.master, bd=5)

        self.container2 = tk.Frame(self.master, bd=5)
        self.container1.pack(fill='both',
                             side="left",
                             expand=1,
                             padx=3,
                             pady=3)
        self.container2.pack(fill='both',
                             side="left",
                             expand=1,
                             padx=3,
                             pady=3)

        # INSERÇÃO E PESQUISA
        self.container3 = tk.Frame(self.container1)
        self.container3.pack(fill='both', expand=1, padx=3, pady=3)

        tk.Label(self.container3, text="ID:").grid(row=0, column=0)
        self.id = tk.Entry(self.container3, state="readonly")
        self.id.grid(row=0, column=1)

        tk.Label(self.container3, text="NOME:").grid(row=1, column=0)
        self.nome = tk.Entry(self.container3)
        self.nome.grid(row=1, column=1)

        tk.Label(self.container3, text="ENDEREÇO:").grid(row=2, column=0)
        self.idade = tk.Entry(self.container3)
        self.idade.grid(row=2, column=1)

        tk.Label(self.container3, text="CPF:").grid(row=3, column=0)
        self.cpf = tk.Entry(self.container3)
        self.cpf.grid(row=3, column=1)

        tk.Label(self.container3, text="E-MAIL:").grid(row=4, column=0)
        self.email = tk.Entry(self.container3)
        self.email.grid(row=4, column=1)

        tk.Label(self.container3, text="FONE:").grid(row=5, column=0)
        self.fone = tk.Entry(self.container3)
        self.fone.grid(row=5, column=1)

        tk.Label(self.container3, text="LOGIN:").grid(row=6, column=0)
        self.cidade = tk.Entry(self.container3)
        self.cidade.grid(row=6, column=1)

        tk.Label(self.container3, text="SENHA:").grid(row=7, column=0)
        self.uf = tk.Entry(self.container3)
        self.uf.grid(row=7, column=1)

        tk.Label(self.container3, text="CNH:").grid(row=8, column=0)
        self.cidade = tk.Entry(self.container3)
        self.cidade.grid(row=8, column=1)

        tk.Label(self.container3, text="NASCIMENTO:").grid(row=9, column=0)
        self.uf = tk.Entry(self.container3)
        self.uf.grid(row=9, column=1)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4, text="INSERIR")
        self.btn_inserir.pack(side="left", expand=1, fill="both")

        self.btn_pesquisar = tk.Button(self.container4, text="PESQUISAR")
        self.btn_pesquisar.pack(side="left", expand=1, fill="both")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
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

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='x')

        self.lista_clientes.pack(fill='x')
        tk.Button(self.container6, text="DELETAR").pack(side="left",
                                                        expand=1,
                                                        fill="both")
        tk.Button(self.container6, text="EDITAR").pack(side="left",
                                                       expand=1,
                                                       fill="both")


class ContratoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.container1 = tk.Frame(self.master, bd=5)

        self.container2 = tk.Frame(self.master, bd=5)
        self.container1.pack(fill='both',
                             side="left",
                             expand=1,
                             padx=3,
                             pady=3)
        self.container2.pack(fill='both',
                             side="left",
                             expand=1,
                             padx=3,
                             pady=3)

        # INSERÇÃO E PESQUISA
        self.container3 = tk.Frame(self.container1)
        self.container3.pack(fill='both', expand=1, padx=3, pady=3)

        tk.Label(self.container3, text="ID CONTRATO:").grid(row=0, column=0)
        self.id = tk.Entry(self.container3, state="readonly")
        self.id.grid(row=0, column=1)

        tk.Label(self.container3, text="ID VEICULO:").grid(row=1, column=0)
        self.nome = tk.Entry(self.container3)
        self.nome.grid(row=1, column=1)

        tk.Label(self.container3, text="ID CLIENTE:").grid(row=2, column=0)
        self.idade = tk.Entry(self.container3)
        self.idade.grid(row=2, column=1)

        tk.Label(self.container3, text="DATA INICIAL:").grid(row=3, column=0)
        self.cpf = tk.Entry(self.container3)
        self.cpf.grid(row=3, column=1)

        tk.Label(self.container3, text="DATA FINAL:").grid(row=4, column=0)
        self.email = tk.Entry(self.container3)
        self.email.grid(row=4, column=1)

        tk.Label(self.container3, text="PREÇO DIÁRIA:").grid(row=5, column=0)
        self.fone = tk.Entry(self.container3)
        self.fone.grid(row=5, column=1)

        tk.Label(self.container3, text="N° DIÁRIA:").grid(row=6, column=0)
        self.cidade = tk.Entry(self.container3)
        self.cidade.grid(row=6, column=1)

        tk.Label(self.container3, text="STATUS:").grid(row=7, column=0)
        self.uf = tk.Entry(self.container3)
        self.uf.grid(row=7, column=1)

        tk.Label(self.container3, text="COMBUSTÍVEL:").grid(row=8, column=0)
        self.comb = tk.Entry(self.container3)
        self.comb.grid(row=8, column=1)

        tk.Label(self.container3, text="PAGAMENTO:").grid(row=9, column=0)
        self.comb = tk.Entry(self.container3)
        self.comb.grid(row=9, column=1)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4, text="INSERIR")
        self.btn_inserir.pack(side="left", expand=1, fill="both")

        self.btn_pesquisar = tk.Button(self.container4, text="PESQUISAR")
        self.btn_pesquisar.pack(side="left", expand=1, fill="both")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
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

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='x')

        self.lista_clientes.pack(fill='x')
        tk.Button(self.container6, text="DELETAR").pack(side="left",
                                                        expand=1,
                                                        fill="both")
        tk.Button(self.container6, text="EDITAR").pack(side="left",
                                                       expand=1,
                                                       fill="both")


class ManutencaoFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.container1 = tk.Frame(self.master, bd=5)

        self.container2 = tk.Frame(self.master, bd=5)
        self.container1.pack(fill='both',
                             side="left",
                             expand=1,
                             padx=3,
                             pady=3)
        self.container2.pack(fill='both',
                             side="left",
                             expand=1,
                             padx=3,
                             pady=3)

        # INSERÇÃO E PESQUISA
        self.container3 = tk.Frame(self.container1)
        self.container3.pack(fill='both', expand=1, padx=3, pady=3)

        tk.Label(self.container3, text="ID :").grid(row=0, column=0)
        self.id = tk.Entry(self.container3, state="readonly")
        self.id.grid(row=0, column=1)

        tk.Label(self.container3, text="MODELO:").grid(row=1, column=0)
        self.nome = tk.Entry(self.container3)
        self.nome.grid(row=1, column=1)

        tk.Label(self.container3, text="CUSTO:").grid(row=2, column=0)
        self.idade = tk.Entry(self.container3)
        self.idade.grid(row=2, column=1)

        tk.Label(self.container3, text="DESCRIÇÃO:").grid(row=3, column=0)
        self.cpf = tk.Entry(self.container3)
        self.cpf.grid(row=3, column=1)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4, text="INSERIR")
        self.btn_inserir.pack(side="left", expand=1, fill="both")

        self.btn_pesquisar = tk.Button(self.container4, text="PESQUISAR")
        self.btn_pesquisar.pack(side="left", expand=1, fill="both")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_clientes = tk.Listbox(self.container5,
                                         yscrollcommand=barraV.set,
                                         xscrollcommand=barraH.set,
                                         selectmode="SINGLE")
        barraV.config(command=self.lista_clientes.yview)
        barraV.pack(side="right", fill='both')

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='both')

        self.lista_clientes.pack(fill='both', expand=1)
        tk.Button(self.container6, text="DELETAR", padx=5,
                  pady=10).pack(side="left", expand=1, fill="x")
        tk.Button(self.container6, text="EDITAR", padx=5,
                  pady=10).pack(side="left", expand=1, fill="x")


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("550x357")
    TelaPrincipalAdmin(app)
    app.mainloop()
