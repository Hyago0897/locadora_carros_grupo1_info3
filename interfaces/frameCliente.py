import tkinter as tk
import tkinter.ttk as ttk
from .entry import CPFEntry, EmailEntry, FoneEntry
from .funcs import *
from tkinter import messagebox


class ClienteFrame(tk.Frame):
    def __init__(self, master, banco):
        tk.Frame.__init__(self, master)
        self.banco = banco
        self.master = master
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

        tk.Label(self.container3, text="CPF:").grid(row=2,
                                                    column=0,
                                                    sticky="e",
                                                    padx=2,
                                                    pady=2)
        self.cpf = CPFEntry(self.container3)
        self.cpf.grid(row=2, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="LOGIN:").grid(row=3,
                                                      column=0,
                                                      sticky="e",
                                                      padx=2,
                                                      pady=2)
        self.login = tk.Entry(self.container3)
        self.login.grid(row=3, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="SENHA:").grid(row=4,
                                                      column=0,
                                                      sticky="e",
                                                      padx=2,
                                                      pady=2)
        self.senha = tk.Entry(self.container3)
        self.senha.grid(row=4, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="E-MAIL:").grid(row=5,
                                                       column=0,
                                                       sticky="e",
                                                       padx=2,
                                                       pady=2)

        self.email = EmailEntry(self.container3)
        self.email.grid(row=5, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="FONE:").grid(row=6,
                                                     column=0,
                                                     sticky="e",
                                                     padx=2,
                                                     pady=2)
        self.fone = FoneEntry(self.container3)
        self.fone.grid(row=6, column=1, sticky="e", padx=2, pady=2)

        tk.Label(self.container3, text="ENDEREÇO:").grid(row=7,
                                                         column=0,
                                                         sticky="e",
                                                         padx=2,
                                                         pady=2)
        self.endereco = tk.Entry(self.container3)
        self.endereco.grid(row=7, column=1, sticky="e", padx=2, pady=2)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='both', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4,
                                     text="INSERIR",
                                     padx=5,
                                     pady=10,
                                     command=self.inserir_cliente)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=5,
                                       pady=10,
                                       command=self.pesquisar_cliente)
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
        self.btn_deletar = tk.Button(
            self.container6,
            text="DELETAR",
            padx=5,
            pady=10,
            command=self.deletar_cliente
        )
        self.btn_deletar.pack(side="left", expand=1, fill="x")
        self.btn_editar = tk.Button(
            self.container6,
            text="EDITAR",
            padx=5,
            pady=10,
            command=self.editar_cliente
        )
        self.btn_editar.pack(side="left", expand=1, fill="x")
        self.atualizar_cliente()

    def valida_dados(self):
        self.obrigatorios = [
            self.nome.get().strip(),
            self.cpf.get().strip(),
            self.login.get().strip(),
            self.senha.get().strip(),
            self.fone.get().strip(),
            self.endereco.get().strip()
        ]
        if all([bool(x)for x in self.obrigatorios]):
            login = self.login.get().strip()
            cpf = self.cpf.get().strip()
            res = self.banco.exe("SELECT login, cpf  FROM cliente").fetchall()
            logins = [x[0] for x in res]
            cpfs = [x[1] for x in res]

            if login not in logins or login == self.editlogin:
                if (cpf not in cpfs or cpf == self.editcpf) and len(cpf) == 14:
                    return True
                else:
                    messagebox.showwarning(
                        "Aviso", f"O cpf '{cpf}' já foi cadastrado!")
                    return False
            else:
                messagebox.showwarning(
                    "Aviso", f"O login '{login}' já foi cadastrado!")
                return False

    def limpar_campos(self):
        self.id["state"] = "normal"
        self.id.delete(0, tk.END)
        self.id["state"] = "readonly"

        self.nome.delete(0, tk.END)
        self.cpf.delete(0, tk.END)
        self.login.delete(0, tk.END)
        self.senha.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.fone.delete(0, tk.END)
        self.endereco.delete(0, tk.END)

    def get_dados(self):
        return {
            "id": self.id.get().strip(),
            "nome": self.nome.get().strip(),
            "cpf": self.cpf.get().strip(),
            "login": self.login.get().strip(),
            "senha": self.senha.get().strip(),
            "email": self.email.get().strip(),
            "fone": self.fone.get().strip(),
            "endereco": self.endereco.get().strip()
        }

    def consulta_dados(self, delimitadores={}):
        pesquisa = """SELECT id, nome, cpf,
                    login, senha, email,
                    fone, endereco
                    FROM CLIENTE"""
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
        UPDATE cliente SET 
        nome='{novos_dados['nome']}',
        cpf='{novos_dados['cpf']}',
        login='{novos_dados['login']}',
        senha='{novos_dados['senha']}',
        email='{novos_dados['email']}',
        fone='{novos_dados['fone']}',
        endereco='{novos_dados['endereco']}'
        WHERE id={novos_dados['id']};"""
        self.banco.exe(comando)

    def insert(self, dados):
        sql = f"""
        INSERT INTO
        CLIENTE({','.join(dados.keys())})
        VALUES('{"','".join(dados.values())}')
        """
        self.banco.exe(sql)

    def delete(self, id):
        sql = f"DELETE FROM CLIENTE WHERE id={id}"
        self.banco.exe(sql)

    def inserir_cliente(self):
        if self.valida_dados():
            dados = self.get_dados()
            del dados['id']
            self.insert(dados)
            messagebox.showinfo(title="Sucesso", message="Registro incluído!")
            self.limpar_campos()
            self.atualizar_cliente()
        else:
            messagebox.showinfo(
                title="Aviso", message="Preencha todos os campos obrigatórios (nome, cpf, login, senha, endereço)")

    def pesquisar_cliente(self):
        dados = self.get_dados()
        resultado = self.consulta_dados(dados)
        self.listar_clientes(resultado)
        self.limpar_campos()

    def editar_cliente(self):
        index = self.lista_clientes.curselection()
        if index:
            dados = self.lista_clientes.get(index, index)[0].split("|")
            dados = [x.strip() for x in dados]

            self.limpar_campos()

            self.id["state"] = "normal"
            self.id.insert(0, dados[0])
            self.id["state"] = "readonly"

            self.nome.insert(0, dados[1])

            self.cpf.insert(0, dados[2])
            self.editcpf = dados[2]

            self.login.insert(0, dados[3])
            self.editlogin = dados[3]

            self.senha.insert(0, dados[4])
            self.email.insert(0, dados[5])
            self.fone.insert(0, dados[6])
            self.endereco.insert(0, dados[7])

            self.btn_inserir['text'] = "SALVAR"
            self.btn_inserir['command'] = self.salvar
            self.btn_pesquisar['text'] = "CANCELAR"
            self.btn_pesquisar['command'] = self.cancelar
            self.btn_deletar.configure(state="disabled")
            self.btn_editar.configure(state="disabled")

            self.lista_clientes.select_clear(0, tk.END)
            self.lista_clientes.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum registro foi selecionado")

    def deletar_cliente(self):
        index = self.lista_clientes.curselection()
        if index:
            id = self.lista_clientes.get(index, index)[0].split("|")[0]
            self.delete(id)

            self.lista_clientes.delete(index)
            self.lista_clientes.select_clear(0, tk.END)
            self.lista_clientes.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum registro foi selecionado")

    def cancelar(self):
        self.btn_deletar.configure(state="normal")
        self.btn_editar.configure(state="normal")
        self.btn_inserir['text'] = "INSERIR"
        self.btn_inserir['command'] = self.inserir_cliente
        self.btn_pesquisar['text'] = "PESQUISAR"
        self.btn_pesquisar['command'] = self.pesquisar_cliente
        self.editlogin = ''
        self.editcpf = ''
        self.limpar_campos()

    def salvar(self):
        if self.valida_dados():
            dados = self.get_dados()
            self.update(dados)
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
            self.cancelar()
            self.atualizar_cliente()

    def atualizar_cliente(self):
        resultado = self.consulta_dados()
        self.listar_clientes(resultado)

    def listar_clientes(self, clientes):
        self.lista_clientes.delete(0, tk.END)
        for cliente in clientes:
            cliente = [str(x) for x in cliente]
            self.lista_clientes.insert(tk.END, " | ".join(cliente))
        self.lista_clientes.select_set(0)
