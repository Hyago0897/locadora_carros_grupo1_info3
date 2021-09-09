from .entry import PlacaEntry
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from datetime import date


class VeiculoFrame(tk.Frame):
    def __init__(self, master, banco):
        tk.Frame.__init__(self, master)
        self.master = master
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
        self.modelo = ttk.Combobox(self.container3, width=19, state="readonly")

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
        self.ano = ttk.Spinbox(
            self.container3, from_=1980, to=date.today().year, width=18, state="readonly")
        self.ano.set('')
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
                                     command=self.inserir_veiculo)
        self.btn_inserir.pack(side="left", expand=1, fill="x")

        self.btn_pesquisar = tk.Button(self.container4,
                                       text="PESQUISAR",
                                       padx=5,
                                       pady=10,
                                       command=self.pesquisar_veiculo)
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
            command=self.deletar_veiculo
        )
        self.btn_deletar.pack(side="left", expand=1, fill="x")
        self.btn_editar = tk.Button(
            self.container6,
            text="EDITAR",
            padx=5,
            pady=10,
            command=self.editar_veiculo
        )
        self.btn_editar.pack(side="left", expand=1, fill="x")

        self.atualizar_veiculo()

    def valida_dados(self):
        self.obrigatorios = [
            self.placa.get().strip(),
            self.marca.get().strip(),
            self.modelo.get().strip(),
            self.cor.get().strip(),
            self.ano.get().strip()
        ]
        if all([bool(x)for x in self.obrigatorios]):
            placa = self.placa.get().strip()
            if len(placa) == 7:
                placas = self.banco.exe("SELECT placa FROM VEICULO")
                placas = [x[0] for x in placas]
                if placa not in placas or placa == self.editplaca:
                    return True
                else:
                    messagebox.showwarning(
                        "Aviso", f"A placa '{placa}' já foi cadastrada!")
        return False

    def lista_modelos(self):
        modelos = self.banco.exe("SELECT modelo FROM MANUTENCAO").fetchall()
        modelos = [x[0] for x in modelos]
        self.modelo.configure(values=modelos)

    def limpar_campos(self):
        self.id["state"] = "normal"
        self.id.delete(0, tk.END)
        self.id["state"] = "readonly"

        self.placa.delete(0, tk.END)
        self.marca.delete(0, tk.END)
        self.modelo.set('')
        self.cor.delete(0, tk.END)

        self.ano.set('')

        self.status["state"] = "normal"
        self.status.delete(0, tk.END)
        self.status["state"] = "readonly"

        self.descricao.delete("1.0", "end-1c")

    def get_dados(self):
        return {
            "id": self.id.get().strip(),
            "placa": self.placa.get().strip(),
            "marca": self.marca.get().strip(),
            "modelo": self.modelo.get().strip(),
            "cor": self.cor.get().strip(),
            "ano": self.ano.get().strip(),
            "status": self.status.get().strip(),
            "descricao": self.descricao.get("1.0", "end-1c").strip()
        }

    def consulta_dados(self, delimitadores={}):
        pesquisa = """SELECT id, placa, marca, 
                      modelo, cor, ano, status,
                      descricao FROM VEICULO """
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
        UPDATE VEICULO SET 
        placa='{novos_dados['placa']}',
        marca='{novos_dados['marca']}',
        modelo='{novos_dados['modelo']}',
        cor='{novos_dados['cor']}',
        ano='{novos_dados['ano']}',
        descricao='{novos_dados['descricao']}'
        WHERE id={novos_dados['id']};"""
        self.banco.exe(comando)

    def insert(self, dados):
        sql = f"""
        INSERT INTO 
        VEICULO({','.join(dados.keys())})
        VALUES ('{"','".join(dados.values())}')
        """
        self.banco.exe(sql)

    def delete(self, id):
        sql = f"DELETE FROM VEICULO WHERE id={id}"
        self.banco.exe(sql)

    def inserir_veiculo(self):
        if self.valida_dados():
            dados = self.get_dados()
            del dados['id']
            dados['status'] = "Disponível"
            self.insert(dados)
            messagebox.showinfo(title="Sucesso", message="Registro incluído!")
            self.limpar_campos()
            self.atualizar_veiculo()
        else:
            messagebox.showinfo(
                title="Aviso", message="Preencha todos os campos obrigatórios (placa, marca, modelo, cor, ano)")

    def pesquisar_veiculo(self):
        dados = self.get_dados()
        resultado = self.consulta_dados(dados)
        self.listar_veiculos(resultado)
        self.limpar_campos()

    def editar_veiculo(self):
        index = self.lista_veiculos.curselection()
        if index:
            dados = self.lista_veiculos.get(index, index)[0].split("|")
            dados = [x.strip() for x in dados]

            self.limpar_campos()

            self.id["state"] = "normal"
            self.id.insert(0, dados[0])
            self.id["state"] = "readonly"

            self.placa.insert(0, dados[1])
            self.editplaca = dados[1]
            self.marca.insert(0, dados[2])

            self.modelo.set(dados[3])

            self.cor.insert(0, dados[4])
            self.ano.set(dados[5])

            self.status["state"] = "normal"
            self.status.insert(0, dados[6])
            self.status["state"] = "readonly"

            self.descricao.insert("1.0", dados[7])

            self.btn_inserir['text'] = "SALVAR"
            self.btn_inserir['command'] = self.salvar
            self.btn_pesquisar['text'] = "CANCELAR"
            self.btn_pesquisar['command'] = self.cancelar
            self.btn_deletar.configure(state="disabled")
            self.btn_editar.configure(state="disabled")

            self.lista_veiculos.select_clear(0, tk.END)
            self.lista_veiculos.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum registro foi selecionado")

    def deletar_veiculo(self):
        index = self.lista_veiculos.curselection()
        if index:
            id = self.lista_veiculos.get(index, index)[0].split("|")[0]
            self.delete(id)

            self.lista_veiculos.delete(index)
            self.lista_veiculos.select_clear(0, tk.END)
            self.lista_veiculos.select_set(0)
        else:
            messagebox.showinfo(title="Informação",
                                message="Nenhum registro foi selecionado")

    def cancelar(self):
        self.btn_deletar.configure(state="normal")
        self.btn_editar.configure(state="normal")
        self.btn_inserir['text'] = "INSERIR"
        self.btn_inserir['command'] = self.inserir_veiculo
        self.btn_pesquisar['text'] = "PESQUISAR"
        self.btn_pesquisar['command'] = self.pesquisar_veiculo
        self.editplaca = ''
        self.limpar_campos()

    def salvar(self):
        if self.valida_dados():
            dados = self.get_dados()
            self.update(dados)
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
            self.cancelar()
            self.atualizar_veiculo()

    def atualizar_veiculo(self):
        self.lista_modelos()
        resultado = self.consulta_dados()
        self.listar_veiculos(resultado)

    def listar_veiculos(self, veiculos):
        self.lista_veiculos.delete(0, tk.END)
        for veiculo in veiculos:
            veiculo = [str(x) for x in veiculo]
            self.lista_veiculos.insert(tk.END, " | ".join(veiculo))
        self.lista_veiculos.select_set(0)
