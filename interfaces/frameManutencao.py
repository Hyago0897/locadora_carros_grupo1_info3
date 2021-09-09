import tkinter as tk
import tkinter.ttk as ttk
from .funcs import *
from tkinter import messagebox


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
        self.modelo = tk.Entry(self.container3, width=19)
        self.modelo.grid(row=1, column=1)

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
        self.descricao = tk.Text(self.container3, width=29, height=7)
        self.descricao.grid(row=4, column=0, columnspan=2)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4,
                                     text="INSERIR",
                                     padx=10,
                                     pady=10,
                                     command=self.inserir_manutencao)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=10,
                                       pady=10,
                                       command=self.pesquisar_manutencao)
        self.btn_pesquisar.pack(side="left", expand=1, fill="x")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_manutencao = tk.Listbox(self.container5,
                                           width=20,
                                           height=11,
                                           yscrollcommand=barraV.set,
                                           xscrollcommand=barraH.set,
                                           selectmode="SINGLE")
        barraV.config(command=self.lista_manutencao.yview)
        barraV.pack(side="right", fill='both')

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_manutencao.xview)
        barraH.pack(side="bottom", fill='both')

        self.lista_manutencao.pack(fill='both', expand=1)
        self.btn_deletar = tk.Button(
            self.container6,
            text="DELETAR",
            padx=5,
            pady=10,
            command=self.deletar_manutencao
        )
        self.btn_deletar.pack(side="left", expand=1, fill="x")
        self.btn_editar = tk.Button(
            self.container6,
            text="EDITAR",
            padx=5,
            pady=10,
            command=self.editar_manutencao
        )
        self.btn_editar.pack(side="left", expand=1, fill="x")
        self.atualizar_manutencao()

    def valida_dados(self):
        self.obrigatorios = [
            self.modelo.get().strip(),
            self.custo.get().strip()
        ]
        if all([bool(x)for x in self.obrigatorios]):
            modelo = self.modelo.get().strip()
            modelos = self.banco.exe(
                "SELECT modelo FROM manutencao").fetchall()
            modelos = [x[0] for x in modelos]

            if modelo not in modelos or modelo == self.editmodelo:
                return True
            else:
                messagebox.showwarning(
                    "Aviso", f"O modelo '{modelo}' já foi cadastrado!")
                return False

    def limpar_campos(self):
        self.modelo.delete(0, tk.END)
        self.custo.delete(0, tk.END)
        self.descricao.delete("1.0", "end-1c")

    def get_dados(self):
        return {
            "modelo": self.modelo.get().strip(),
            "custo": self.custo.get().strip(),
            "descricao": self.descricao.get("1.0", "end-1c").strip()
        }

    def consulta_dados(self, delimitadores={}):
        pesquisa = """SELECT modelo, custo, descricao
                    FROM MANUTENCAO"""
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
        UPDATE manutencao SET 
        custo='{novos_dados['custo']}',
        descricao='{novos_dados['descricao']}'
        WHERE modelo='{novos_dados['modelo']}';"""
        self.banco.exe(comando)

    def insert(self, dados):
        sql = f"""
        INSERT INTO
        MANUTENCAO({','.join(dados.keys())})
        VALUES('{"','".join(dados.values())}')
        """
        self.banco.exe(sql)

    def delete(self, modelo):
        sql = f"DELETE FROM MANUTENCAO WHERE modelo={modelo}"
        self.banco.exe(sql)

    def inserir_manutencao(self):
        if self.valida_dados():
            dados = self.get_dados()
            self.insert(dados)
            messagebox.showinfo(title="Sucesso", message="Registro incluído!")
            self.limpar_campos()
            self.atualizar_manutencao()
        else:
            messagebox.showinfo(
                title="Aviso", message="Preencha todos os campos obrigatórios (modelo, cpf, login, senha, endereço)")

    def pesquisar_manutencao(self):
        dados = self.get_dados()
        resultado = self.consulta_dados(dados)
        self.listar_manutencoes(resultado)
        self.limpar_campos()

    def editar_manutencao(self):
        index = self.lista_manutencao.curselection()
        if index:
            dados = self.lista_manutencao.get(index, index)[0].split("|")
            dados = [x.strip() for x in dados]

            self.limpar_campos()

            self.modelo.insert(0, dados[0])
            self.editmodelo = dados[0]

            self.custo.insert(0, dados[1])
            self.descricao.insert("1.0", dados[2])

            self.btn_inserir['text'] = "SALVAR"
            self.btn_inserir['command'] = self.salvar
            self.btn_pesquisar['text'] = "CANCELAR"
            self.btn_pesquisar['command'] = self.cancelar
            self.btn_deletar.configure(state="disabled")
            self.btn_editar.configure(state="disabled")

            self.lista_manutencao.select_clear(0, tk.END)
            self.lista_manutencao.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum registro foi selecionado")

    def deletar_manutencao(self):
        index = self.lista_manutencao.curselection()
        if index:
            id = self.lista_manutencao.get(index, index)[0].split("|")[0]
            self.delete(id)

            self.lista_manutencao.delete(index)
            self.lista_manutencao.select_clear(0, tk.END)
            self.lista_manutencao.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum registro foi selecionado")

    def cancelar(self):
        self.btn_deletar.configure(state="normal")
        self.btn_editar.configure(state="normal")
        self.btn_inserir['text'] = "INSERIR"
        self.btn_inserir['command'] = self.inserir_manutencao
        self.btn_pesquisar['text'] = "PESQUISAR"
        self.btn_pesquisar['command'] = self.pesquisar_manutencao
        self.editmodelo = ''
        self.limpar_campos()

    def salvar(self):
        if self.valida_dados():
            dados = self.get_dados()
            self.update(dados)
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
            self.cancelar()
            self.atualizar_manutencao()

    def atualizar_manutencao(self):
        resultado = self.consulta_dados()
        self.listar_manutencoes(resultado)

    def listar_manutencoes(self, manutencaos):
        self.lista_manutencao.delete(0, tk.END)
        for manutencao in manutencaos:
            manutencao = [str(x) for x in manutencao]
            self.lista_manutencao.insert(tk.END, " | ".join(manutencao))
        self.lista_manutencao.select_set(0)
