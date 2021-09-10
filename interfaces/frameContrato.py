import tkinter as tk
import tkinter.ttk as ttk
from .funcs import *
from .entry import SimpleDateEntry
from tkinter import messagebox
from datetime import datetime


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

        tk.Label(self.container3, text="ID_VEICULO:").grid(row=1,
                                                           column=0,
                                                           sticky="e")
        self.id_veiculo = ttk.Combobox(
            self.container3, width=19, state="readonly")
        self.id_veiculo.grid(row=1, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="ID_CLIENTE:").grid(row=2,
                                                           column=0,
                                                           sticky="e",
                                                           padx=2,
                                                           pady=2)
        self.id_cliente = ttk.Combobox(
            self.container3, width=19, state="readonly")
        self.id_cliente.grid(row=2, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="DATA INICIAL:").grid(row=3,
                                                             column=0,
                                                             sticky="e",
                                                             padx=2,
                                                             pady=2)
        self.inicio = SimpleDateEntry(self.container3)
        self.inicio.grid(row=3, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="DATA FINAL:").grid(row=4,
                                                           column=0,
                                                           sticky="e",
                                                           padx=2,
                                                           pady=2)
        self.termino = SimpleDateEntry(self.container3)
        self.termino.grid(row=4, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="DIÁRIA (R$):").grid(row=5,
                                                            column=0,
                                                            sticky="e",
                                                            padx=2,
                                                            pady=2)
        self.diaria = tk.Entry(self.container3, validate="key")
        self.diaria.configure(validatecommand=(self.diaria.register(valida_valor),
                                               "%P"))
        self.diaria.grid(row=5, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="N° DIÁRIA:").grid(row=6,
                                                          column=0,
                                                          sticky="e")
        self.n_diarias = tk.Entry(self.container3, state="readonly")
        self.n_diarias.grid(row=6, column=1, padx=2, pady=2)

        tk.Label(self.container3, text="STATUS:").grid(row=7,
                                                       column=0,
                                                       sticky="e")
        self.status = tk.Entry(self.container3, state="readonly")
        self.status.grid(row=7, column=1, padx=2, pady=2)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4,
                                     text="INSERIR",
                                     padx=5,
                                     pady=10,
                                     command=self.inserir_contrato)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=5,
                                       pady=10,
                                       command=self.pesquisar_contrato)
        self.btn_pesquisar.pack(side="left", expand=1, fill="x")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_contratos = tk.Listbox(self.container5,
                                          width=20,
                                          height=11,
                                          yscrollcommand=barraV.set,
                                          xscrollcommand=barraH.set,
                                          selectmode="SINGLE")
        barraV.config(command=self.lista_contratos.yview)
        barraV.pack(side="right", fill='y')

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_contratos.xview)
        barraH.pack(side="bottom", fill='x')

        self.lista_contratos.pack(fill='both', expand=1)
        self.btn_deletar = tk.Button(
            self.container6,
            text="DELETAR",
            padx=5,
            pady=10,
            command=self.deletar_contrato
        )
        self.btn_deletar.pack(side="left", expand=1, fill="x")
        self.btn_editar = tk.Button(
            self.container6,
            text="EDITAR",
            padx=5,
            pady=10,
            command=self.editar_contrato
        )
        self.btn_editar.pack(side="left", expand=1, fill="x")
        self.atualizar_contrato()

    def valida_dados(self):
        self.obrigatorios = [
            self.id_veiculo.get().strip(),
            self.id_cliente.get().strip(),
            self.inicio.get().strip(),
            self.termino.get().strip(),
            self.diaria.get().strip()
        ]
        if all([bool(x)for x in self.obrigatorios]):
            inicio = self.inicio.get().strip()
            termino = self.termino.get().strip()
            if len(inicio) == 10 and len(termino) == 10:
                return True
        else:
            return False

    def lista_id_veiculos(self):
        id_veiculos = self.banco.exe("SELECT id FROM veiculo").fetchall()
        id_veiculos = [x[0] for x in id_veiculos]
        self.id_veiculo.configure(values=id_veiculos)

    def lista_id_clientes(self):
        id_clientes = self.banco.exe("SELECT id FROM cliente").fetchall()
        id_clientes = [x[0] for x in id_clientes]
        self.id_cliente.configure(values=id_clientes)

    def limpar_campos(self):
        self.id["state"] = "normal"
        self.id.delete(0, tk.END)
        self.id["state"] = "readonly"

        self.id_veiculo["state"] = "normal"
        self.id_veiculo.delete(0, tk.END)
        self.id_veiculo["state"] = "readonly"

        self.id_cliente["state"] = "normal"
        self.id_cliente.delete(0, tk.END)
        self.id_cliente["state"] = "readonly"

        self.inicio.delete(0, tk.END)
        self.termino.delete(0, tk.END)
        self.diaria.delete(0, tk.END)

        self.n_diarias["state"] = "normal"
        self.n_diarias.delete(0, tk.END)
        self.n_diarias["state"] = "readonly"

        self.status["state"] = "normal"
        self.status.delete(0, tk.END)
        self.status["state"] = "readonly"

    def get_dados(self):
        date_format = "%d/%m/%Y"
        inicio = datetime.strptime(self.inicio.get().strip(), date_format)
        fim = datetime.strptime(self.termino.get().strip(), date_format)
        diff = inicio - fim

        return {
            "id": self.id.get().strip(),
            "id_veiculo": self.id_veiculo.get().strip(),
            "id_cliente": self.id_cliente.get().strip(),
            "inicio": self.inicio.get().strip(),
            "termino": self.termino.get().strip(),
            "diaria": self.diaria.get().strip(),
            "n_diarias": str(abs(diff.days)),
            "status": self.status.get().strip()
        }

    def consulta_dados(self, delimitadores={}):
        pesquisa = """SELECT id, id_veiculo, id_cliente, 
                      inicio, termino, diaria, n_diarias,
                      status FROM contrato """
        if delimitadores:
            pesquisa += " WHERE "
            parcelas = []
            for key, value in delimitadores.items():
                parcelas.append(f"{key} like '%{value}%'")
            pesquisa += " AND ".join(parcelas)
        consulta = self.banco.exe(pesquisa+";")
        return consulta.fetchall()

    def update(self, novos_dados):
        comando = f"""
        UPDATE CONTRATO SET 
        id_veiculo='{novos_dados['id_veiculo']}',
        id_cliente='{novos_dados['id_cliente']}',
        inicio='{novos_dados['inicio']}',
        termino='{novos_dados['termino']}',
        diaria='{novos_dados['diaria']}',
        n_diarias='{novos_dados['n_diarias']}'
        WHERE id={novos_dados['id']};"""
        self.banco.exe(comando)

    def insert(self, dados):
        sql = f"""
        INSERT INTO 
        CONTRATO({','.join(dados.keys())})
        VALUES ('{"','".join(dados.values())}')
        """
        self.banco.exe(sql)

    def delete(self, id):
        sql = f"DELETE FROM CONTRATO WHERE id={id};"
        self.banco.exe(sql)

    def inserir_contrato(self):
        if self.valida_dados():
            dados = self.get_dados()
            del dados['id']
            dados['status'] = "Disponível"
            self.insert(dados)
            messagebox.showinfo(title="Sucesso", message="Registro incluído!")
            self.limpar_campos()
            self.atualizar_contrato()
        else:
            messagebox.showinfo(
                title="Aviso", message="Preencha todos os campos obrigatórios (contrato, id_cliente, inicio, termino, diaria, n_diarias)")

    def pesquisar_contrato(self):
        dados = self.get_dados()
        resultado = self.consulta_dados(dados)
        self.listar_contratos(resultado)
        self.limpar_campos()

    def editar_contrato(self):
        index = self.lista_contratos.curselection()
        if index:
            dados = self.lista_contratos.get(index, index)[0].split("|")
            dados = [x.strip() for x in dados]

            self.limpar_campos()

            self.id["state"] = "normal"
            self.id.insert(0, dados[0])
            self.id["state"] = "readonly"

            self.id_veiculo["state"] = "normal"
            self.id_veiculo.insert(0, dados[1])
            self.id_veiculo["state"] = "readonly"

            self.id_cliente["state"] = "normal"
            self.id_cliente.insert(0, dados[2])
            self.id_cliente["state"] = "readonly"

            self.inicio.insert(0, dados[3])
            self.termino.insert(0, dados[4])

            self.diaria.insert(0, dados[5])

            self.n_diarias["state"] = "normal"
            self.n_diarias.insert(0, dados[6])
            self.n_diarias["state"] = "readonly"

            self.status["state"] = "normal"
            self.status.insert(0, dados[7])
            self.status["state"] = "readonly"

            self.btn_inserir['text'] = "SALVAR"
            self.btn_inserir['command'] = self.salvar
            self.btn_pesquisar['text'] = "CANCELAR"
            self.btn_pesquisar['command'] = self.cancelar
            self.btn_deletar.configure(state="disabled")
            self.btn_editar.configure(state="disabled")

            self.lista_contratos.select_clear(0, tk.END)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum registro foi selecionado")

    def deletar_contrato(self):
        index = self.lista_contratos.curselection()
        if index:
            id = self.lista_contratos.get(index, index)[
                0].split("|")[0].strip()
            self.delete(id)

            self.lista_contratos.delete(index)
            self.lista_contratos.select_clear(0, tk.END)
            self.lista_contratos.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum registro foi selecionado")

    def cancelar(self):
        self.btn_deletar.configure(state="normal")
        self.btn_editar.configure(state="normal")
        self.btn_inserir['text'] = "INSERIR"
        self.btn_inserir['command'] = self.inserir_contrato
        self.btn_pesquisar['text'] = "PESQUISAR"
        self.btn_pesquisar['command'] = self.pesquisar_contrato
        self.limpar_campos()

    def salvar(self):
        if self.valida_dados():
            dados = self.get_dados()
            self.update(dados)
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
            self.cancelar()
            self.atualizar_contrato()

    def atualizar_contrato(self):
        self.lista_id_clientes()
        self.lista_id_veiculos()
        resultado = self.consulta_dados()
        self.listar_contratos(resultado)

    def listar_contratos(self, contratos):
        self.lista_contratos.delete(0, tk.END)
        for contrato in contratos:
            contrato = [str(x) for x in contrato]
            self.lista_contratos.insert(tk.END, " | ".join(contrato))
        self.lista_contratos.select_clear(0, tk.END)
