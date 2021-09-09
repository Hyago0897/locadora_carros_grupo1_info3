import tkinter as tk
import tkinter.ttk as ttk
from .funcs import *


class ManutencaoFrame(tk.Frame):
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

