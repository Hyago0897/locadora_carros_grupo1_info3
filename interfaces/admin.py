import datetime
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from .frameVeiculo import VeiculoFrame
from .frameCliente import ClienteFrame
from .frameContrato import ContratoFrame
from .frameManutencao import ManutencaoFrame



class TelaPrincipalAdmin(tk.Frame):
    def __init__(self, master, banco):
        tk.Frame.__init__(self, master)
        self.master = master
        self.banco = banco
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

        self.logout = tk.Button(self.container1, text="Logout")
        self.logout.pack(side="right", fill="both", padx=3, pady=3)

        # Veiculos
        self.veiculo = VeiculoFrame(self.painel_veiculo, self.banco)
        # Clientes
        self.cliente = ClienteFrame(self.painel_cliente, self.banco)
        # Contratos
        self.contrato = ContratoFrame(self.painel_contrato, self.banco)
        # Manutenções
        self.manutencao = ManutencaoFrame(self.painel_manutencao, self.banco)

    def pref(self):
        pass

    def renomear(self, login):
        novo = self.banco.cursor.execute(
            "SELECT nome FROM admin WHERE login=" + repr(login)).fetchone()[0]
        self.nomeAdm.configure(text="Admin: " + str(novo))


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("560x410")
    TelaPrincipalAdmin(app)
    app.mainloop()
