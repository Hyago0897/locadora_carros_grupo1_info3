from .entry import PlacaEntry
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class VeiculoFrame(tk.Frame):
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
        self.id.grid(row=0, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="PLACA:").grid(row=1,
                                                      column=0,
                                                      sticky="e",
                                                      padx=2,
                                                      pady=2)
        self.placa = PlacaEntry(self.container3)
        self.placa.grid(row=1, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="MARCA:").grid(row=2,
                                                      column=0,
                                                      sticky="e",
                                                      padx=2,
                                                      pady=2)
        self.marca = tk.Entry(self.container3)
        self.marca.grid(row=2, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="MODELO:").grid(row=3,
                                                       column=0,
                                                       sticky="e",
                                                       padx=2,
                                                       pady=2)
        self.modelo = ttk.Combobox(self.container3, width=19)
        self.modelo.grid(row=3, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="COR:").grid(row=4,
                                                    column=0,
                                                    sticky="e",
                                                    padx=2,
                                                    pady=2)
        self.cor = tk.Entry(self.container3)
        self.cor.grid(row=4, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="ANO:").grid(row=5,
                                                    column=0,
                                                    sticky="e",
                                                    padx=2,
                                                    pady=2)
        self.ano = tk.Entry(self.container3)
        self.ano.grid(row=5, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="STATUS:").grid(row=6,
                                                       column=0,
                                                       sticky="e",
                                                       padx=2,
                                                       pady=2)
        self.status = tk.Entry(self.container3, state="readonly")
        self.status.grid(row=6, column=1, sticky="w", padx=2, pady=2)

        tk.Label(self.container3, text="DESCRIÇÃO:").grid(row=7,
                                                          column=0,
                                                          sticky="e",
                                                          padx=2,
                                                          pady=2)
        self.descricao = tk.Text(self.container3, width=31, height=2)
        self.descricao.grid(row=8, column=0, columnspan=2, padx=2, pady=2)

        self.container4 = tk.Frame(self.container1)
        self.container4.pack(fill='x', expand=1, padx=3, pady=3)
        self.btn_inserir = tk.Button(self.container4,
                                     text="INSERIR",
                                     padx=5,
                                     pady=10,
                                     command=self.inserir)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=5,
                                       pady=10,
                                       command=self.pesquisar)
        self.btn_pesquisar.pack(side="left", expand=1, fill="x")

        # VISUALIZAR REGISTROS
        self.container5 = tk.Frame(self.container2)
        self.container5.pack(fill='both', expand=1)

        barraV = tk.Scrollbar(self.container5, orient="vertical")
        barraH = tk.Scrollbar(self.container5, orient="horizontal")
        self.lista_veiculos = tk.Listbox(self.container5,
                                         width=30,
                                         height=13,
                                         yscrollcommand=barraV.set,
                                         xscrollcommand=barraH.set,
                                         selectmode="SINGLE")
        barraV.config(command=self.lista_veiculos.yview)
        barraV.pack(side="right", fill='both')

        self.container6 = tk.Frame(self.container2)
        self.container6.pack(side="bottom", fill='both', expand=1)

        barraH.config(command=self.lista_veiculos.xview)
        barraH.pack(side="bottom", fill='both')

        self.lista_veiculos.pack(fill='both', expand=1)
        self.btn_deletar = tk.Button(
            self.container6,
            text="DELETAR",
            padx=5,
            pady=10,
            command=self.deletar
        )
        self.btn_deletar.pack(side="left", expand=1, fill="x")
        self.btn_editar = tk.Button(
            self.container6,
            text="EDITAR",
            padx=5,
            pady=10,
            command=self.editar
        )
        self.btn_editar.pack(side="left", expand=1, fill="x")

    def limpar_campos(self):
        self.id.delete(0, tk.END)
        self.placa.delete(0, tk.END)
        self.marca.delete(0, tk.END)
        self.modelo.delete(0, tk.END)
        self.cor.delete(0, tk.END)
        self.ano.delete(0, tk.END)
        self.status.delete(0, tk.END)
        self.descricao.delete(0, tk.END)

    def get_dados(self):
        return {
            "placa": self.placa.get().strip(),
            "marca": self.marca.get().strip(),
            "modelo": self.modelo.get().strip(),
            "cor": self.cor.get().strip(),
            "ano": self.ano.get().strip(),
            "status": self.status.get().strip(),
            "descricao": self.descricao.get("1.0", "end-1c").strip()
        }

    def valida_dados(self):
        self.obrigatorios = [
            self.placa.get().strip(),
            self.marca.get().strip(),
            self.modelo.get().strip(),
            self.cor.get().strip(),
            self.ano.get().strip()
        ]
        if all([bool(x)for x in self.obrigatorios]):
            if len(self.placa.get()) == 7:
                dic = {}
                return True
            else:
                return False

    def consulta_dados(self, delimitadores={}):
        pesquisa = "SELECT * FROM VEICULOS"
        if delimitadores:
            pesquisa += " WHERE "
            parcelas = []
            for key, value in delimitadores.items():
                parcelas.append(f"{key} like '%{value}%'")
            pesquisa += " AND ".join(parcelas)

        # print(pesquisa)
        consulta = self.db.cursor.execute(pesquisa+";")
        return consulta.fetchall()

    def update(self, novos_dados):
        comando = f"""
        UPDATE VEICULOS SET 
        placa='{novos_dados['placa']}',
        marca='{novos_dados['marca']}',
        modelo='{novos_dados['modelo']}',
        cor='{novos_dados['cor']}',
        ano='{novos_dados['ano']}',
        descricao='{novos_dados['descricao']}'
        WHERE id={novos_dados['id']};"""
        self.db.cursor.execute(comando)
        self.db.commit()

    def insert(self, dados):
        if self.valida_dados():
            sql = f"""
            INSERT INTO 
            VEICULO({','.join(dados.keys())})
            VALUES ('{','.join(dados.values())}')
            """
            self.banco.cursor.execute(sql)
            self.banco.cursor.commit()

    def delete(self, id):
        sql = f"DELETE FROM VEICULO WHERE id={id}"
        self.banco.cursor.execute(sql)
        self.banco.cursor.commit()

    def inserir(self):
        if self.valida_dados():
            dados = self.get_dados()
            dados['status'] = "Disponível"
            self.insert(dados)
            messagebox.showinfo(title="Sucesso", text="Registro incluído!")
        else:
            messagebox.showinfo(
                title="Aviso", message="Preencha todos os campos obrigatórios (placa, marca, modelo, cor, ano)")

    def editar(self):
        index = self.lista_veiculos.curselection()
        if index:
            dados = self.lista_veiculos.get(index, index)[0].split("|")
            dados = [x.strip() for x in dados]

            self.limpar_campos()

            self.id["state"] = "normal"
            self.id.insert(0, dados[0])
            self.id["state"] = "readonly"

            self.placa.insert(0, dados[1])
            self.marca.insert(0, dados[2])
            self.modelo.insert(0, dados[3])
            self.cor.insert(0, dados[4])
            self.ano.insert(0, dados[5])
            self.status.insert(0, dados[6])
            self.descricao.insert(0, dados[7])

            self.btn_inserir['text'] = "SALVAR"
            self.btn_inserir['command'] = self.salvar
            self.btn_pesquisar['text'] = "CANCELAR"
            self.btn_pesquisar['command'] = self.cancelar

            self.lista_veiculos.select_clear(0, tk.END)
            self.lista_veiculos.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum usuário foi selecionado")

    def cancelar(self):
        self.btn_inserir['text'] = "INSERIR"
        self.btn_inserir['command'] = self.inserir_veiculo
        self.btn_pesquisar['text'] = "PESQUISAR"
        self.btn_pesquisar['command'] = self.pesquisar_veiculo

        self.limpar_campos()

    def pesquisar(self):
        pass

    def deletar(self):
        pass

    def limpar_campos(self):
        self.id["state"] = "normal"
        self.id.delete(0, tk.END)
        self.id["state"] = "readonly"

        self.nome.delete(0, tk.END)
        self.idade.delete(0, tk.END)
        self.cpf.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.fone.delete(0, tk.END)
        self.cidade.delete(0, tk.END)
        self.uf.delete(0, tk.END)

    def salvar(self):
        if self.verifica_valores():
            dados = {
                'id': self.id.get().strip(),
                'nome': self.nome.get().strip(),
                'idade': self.idade.get().strip(),
                'cpf': self.cpf.get().strip(),
                'email': self.email.get().strip(),
                'fone': self.fone.get().strip(),
                'cidade': self.cidade.get().strip(),
                'uf': self.uf.get().strip()
            }
            self.banco.atualizar_dados(dados)
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
            self.cancelar()
            self.atualizar_clientes()

    def atualizar_clientes(self):
        resultado = self.banco.consulta_dados()
        self.listar_clientes(resultado)

    def listar_clientes(self, clientes):
        self.lista_clientes.delete(0, tk.END)
        for cliente in clientes:
            cliente = [str(x) for x in cliente]
            self.lista_clientes.insert(tk.END, " | ".join(cliente))
        self.lista_clientes.select_set(0)

    def deletar_cliente(self):
        index = self.lista_clientes.curselection()
        if index:
            id = self.lista_clientes.get(index, index)[0].split("|")[0]
            self.banco.deletar_dados(id)

            self.lista_clientes.delete(index)
            self.lista_clientes.select_clear(0, tk.END)
            self.lista_clientes.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum usuário foi selecionado")
