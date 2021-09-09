import datetime
import re
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
        self.prog.add_command(label="Fechar", command=lambda x: print("12"))
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

        self.nomeAdm = tk.Label(self.container1,
                                text="Admin: ",
                                font="Default 10")
        self.nomeAdm.pack(side="left", fill="both", padx=3, pady=3)

        tk.Button(self.container1, text="Logout").pack(side="right",
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

    def pref(self):
        pass

    def renomear(self, novo):
        self.nomeAdm.configure(text="Admin: " + str(novo))


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

        tk.Label(self.container3, text="ID:").grid(row=0,
                                                   column=0,
                                                   sticky="e",
                                                   padx=2,
                                                   pady=2)
        self.id = tk.Entry(self.container3, state="readonly")
        self.id.grid(row=0, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="PLACA:").grid(row=1,
                                                      column=0,
                                                      sticky="e",
                                                      padx=2,
                                                      pady=2)
        self.nome = PlacaEntry(self.container3)
        self.nome.grid(row=1, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="MARCA:").grid(row=2,
                                                      column=0,
                                                      sticky="e",
                                                      padx=2,
                                                      pady=2)
        self.idade = tk.Entry(self.container3)
        self.idade.grid(row=2, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="MODELO:").grid(row=3,
                                                       column=0,
                                                       sticky="e",
                                                       padx=2,
                                                       pady=2)
        self.cpf = ttk.Combobox(self.container3, width=19)
        self.cpf.grid(row=3, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="COR:").grid(row=4,
                                                    column=0,
                                                    sticky="e",
                                                    padx=2,
                                                    pady=2)
        self.email = tk.Entry(self.container3)
        self.email.grid(row=4, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="ANO:").grid(row=5,
                                                    column=0,
                                                    sticky="e",
                                                    padx=2,
                                                    pady=2)
        self.fone = tk.Entry(self.container3)
        self.fone.grid(row=5, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="STATUS:").grid(row=6,
                                                       column=0,
                                                       sticky="e",
                                                       padx=2,
                                                       pady=2)
        self.uf = tk.Entry(self.container3, state="readonly")
        self.uf.grid(row=6, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="DESCRIÇÃO:").grid(row=7,
                                                          column=0,
                                                          sticky="e",
                                                          padx=2,
                                                          pady=2)
        self.cidade = tk.Text(self.container3, width=31, height=2)
        self.cidade.grid(row=8, column=0, columnspan=2, padx=2, pady=2)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='x', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4,
                                     text="INSERIR",
                                     padx=5,
                                     pady=10)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=5,
                                       pady=10)
        self.btn_pesquisar.pack(side="left", expand=1, fill="x")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_clientes = tk.Listbox(self.container5,
                                         width=30,
                                         height=13,
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
            padx=5,
            pady=10,
        ).pack(side="left", expand=1, fill="x")
        tk.Button(
            self.container6,
            text="EDITAR",
            padx=5,
            pady=10,
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
        self.container3.pack(fill='x', expand=1, padx=3, pady=3)

        tk.Label(self.container3, text="ID:").grid(row=0,
                                                   column=0,
                                                   sticky="e",
                                                   padx=2,
                                                   pady=2)
        self.id = tk.Entry(self.container3, state="readonly")
        self.id.grid(row=0, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="NOME:").grid(row=1,
                                                     column=0,
                                                     sticky="e",
                                                     padx=2,
                                                     pady=2)
        self.nome = tk.Entry(self.container3)
        self.nome.grid(row=1, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="ENDEREÇO:").grid(row=2,
                                                         column=0,
                                                         sticky="e",
                                                         padx=2,
                                                         pady=2)
        self.idade = tk.Entry(self.container3)
        self.idade.grid(row=2, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="CPF:").grid(row=3,
                                                    column=0,
                                                    sticky="e",
                                                    padx=2,
                                                    pady=2)
        self.cpf = CPFEntry(self.container3)
        self.cpf.grid(row=3, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="E-MAIL:").grid(row=4,
                                                       column=0,
                                                       sticky="e",
                                                       padx=2,
                                                       pady=2)

        self.email = EmailEntry(self.container3)
        self.email.grid(row=4, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="FONE:").grid(row=5,
                                                     column=0,
                                                     sticky="e",
                                                     padx=2,
                                                     pady=2)
        self.fone = FoneEntry(self.container3)
        self.fone.grid(row=5, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="LOGIN:").grid(row=6,
                                                      column=0,
                                                      sticky="e",
                                                      padx=2,
                                                      pady=2)
        self.cidade = tk.Entry(self.container3)
        self.cidade.grid(row=6, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="SENHA:").grid(row=7,
                                                      column=0,
                                                      sticky="e",
                                                      padx=2,
                                                      pady=2)
        self.uf = tk.Entry(self.container3)
        self.uf.grid(row=7, column=1, sticky="e", padx=2, pady=2)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4,
                                     text="INSERIR",
                                     padx=5,
                                     pady=10)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=5,
                                       pady=10)
        self.btn_pesquisar.pack(side="left", expand=1, fill="x")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_clientes = tk.Listbox(self.container5,
                                         width=20,
                                         height=11,
                                         yscrollcommand=barraV.set,
                                         xscrollcommand=barraH.set,
                                         selectmode="SINGLE")
        barraV.config(command=self.lista_clientes.yview)
        barraV.pack(side="right", fill='y')

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='x')

        self.lista_clientes.pack(fill='both', expand=1)
        tk.Button(self.container6, text="DELETAR", padx=5,
                  pady=10).pack(side="left", expand=1, fill="x")
        tk.Button(self.container6, text="EDITAR", padx=5,
                  pady=10).pack(side="left", expand=1, fill="x")


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
        self.container3.pack(fill='x', expand=1, padx=3, pady=3)

        tk.Label(self.container3, text="ID:").grid(row=0,
                                                   column=0,
                                                   sticky="e",
                                                   padx=2,
                                                   pady=2)
        self.id = tk.Entry(self.container3, state="readonly")
        self.id.grid(row=0, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="VEICULO:").grid(row=1,
                                                        column=0,
                                                        sticky="e")
        self.nome = ttk.Combobox(self.container3, width=19)
        self.nome.grid(row=1, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="CLIENTE:").grid(row=2,
                                                        column=0,
                                                        sticky="e",
                                                        padx=2,
                                                        pady=2)
        self.idade = ttk.Combobox(self.container3, width=19)
        self.idade.grid(row=2, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="DATA INICIAL:").grid(row=3,
                                                             column=0,
                                                             sticky="e",
                                                             padx=2,
                                                             pady=2)
        self.cpf = SimpleDateEntry(self.container3)
        self.cpf.grid(row=3, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="DATA FINAL:").grid(row=4,
                                                           column=0,
                                                           sticky="e",
                                                           padx=2,
                                                           pady=2)
        self.email = SimpleDateEntry(self.container3)
        self.email.grid(row=4, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="DIÁRIA (R$):").grid(row=5,
                                                            column=0,
                                                            sticky="e",
                                                            padx=2,
                                                            pady=2)
        self.fone = tk.Entry(self.container3, validate="key")
        self.fone.configure(validatecommand=(self.fone.register(valida_valor),
                                             "%P"))
        self.fone.grid(row=5, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="N° DIÁRIA:").grid(row=6,
                                                          column=0,
                                                          sticky="e")
        self.cidade = tk.Entry(self.container3, state="readonly")
        self.cidade.grid(row=6, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="STATUS:").grid(row=7,
                                                       column=0,
                                                       sticky="e")
        self.uf = tk.Entry(self.container3, state="readonly")
        self.uf.grid(row=7, column=1, padx=2, pady=2)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4,
                                     text="INSERIR",
                                     padx=5,
                                     pady=10)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=5,
                                       pady=10)
        self.btn_pesquisar.pack(side="left", expand=1, fill="x")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_clientes = tk.Listbox(self.container5,
                                         width=20,
                                         height=11,
                                         yscrollcommand=barraV.set,
                                         xscrollcommand=barraH.set,
                                         selectmode="SINGLE")
        barraV.config(command=self.lista_clientes.yview)
        barraV.pack(side="right", fill='y')

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='x')

        self.lista_clientes.pack(fill='both', expand=1)
        tk.Button(self.container6, text="DELETAR", padx=5,
                  pady=10).pack(side="left", expand=1, fill="x")
        tk.Button(self.container6, text="EDITAR", padx=5,
                  pady=10).pack(side="left", expand=1, fill="x")


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
        self.container3.pack(expand=1, padx=3, pady=3)

        tk.Label(self.container3, text="MODELO:").grid(row=1,
                                                       column=0,
                                                       sticky="e",
                                                       padx=3,
                                                       pady=3)
        self.nome = tk.Entry(self.container3, width=19)
        self.nome.grid(row=1, column=1)

        tk.Label(self.container3, text="CUSTO (R$):").grid(row=2,
                                                           column=0,
                                                           sticky="e",
                                                           padx=3,
                                                           pady=3)

        self.custo = tk.Entry(self.container3, width=19, validate="key")
        self.custo.configure(
            validatecommand=(self.custo.register(valida_valor), '%P'))

        self.custo.grid(row=2, column=1)

        tk.Label(self.container3, text="DESCRIÇÃO:").grid(row=3,
                                                          column=0,
                                                          sticky="e",
                                                          padx=3,
                                                          pady=3)
        self.cpf = tk.Text(self.container3, width=29, height=7)
        self.cpf.grid(row=4, column=0, columnspan=2)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4,
                                     text="INSERIR",
                                     padx=10,
                                     pady=10)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=10,
                                       pady=10)
        self.btn_pesquisar.pack(side="left", expand=1, fill="x")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_clientes = tk.Listbox(self.container5,
                                         width=20,
                                         height=11,
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


class SimpleDateEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, master=mst, **kwargs)

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
                if self.get()[6:10] < "2000":
                    self.delete(6, tk.END)
                    self.insert(6, "2000")
                if self.get()[3:5] == "02":
                    if SimpleDateEntry.ehbissexto(int(self.get()[6:10])):
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


class PlacaEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, mst, **kwargs)

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
                if self.get()[6:10] < "2000":
                    self.delete(6, tk.END)
                    self.insert(6, "2000")
                if self.get()[3:5] == "02":
                    if SimpleDateEntry.ehbissexto(int(self.get()[6:10])):
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


class CPFEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, mst, **kwargs)


class EmailEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, mst, **kwargs)


class FoneEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, mst, **kwargs)


def valida_valor(valor):
    regex = re.compile(r"\d+(\.\d{,2})?$")
    res = regex.match(valor)
    return valor == '' or res is not None


def valida_email(email):
    regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    res = regex.match(email)
    return email == '' or res is not None


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("560x410")
    TelaPrincipalAdmin(app)
    app.mainloop()
