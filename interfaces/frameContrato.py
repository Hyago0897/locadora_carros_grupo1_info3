import tkinter as tk
import tkinter.ttk as ttk
from .funcs import *
from .entry import SimpleDateEntry


class ContratoFrame(tk.Frame):
    def __init__(self, master, banco):
        tk.Frame.__init__(self, master)
        self.banco = banco
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
