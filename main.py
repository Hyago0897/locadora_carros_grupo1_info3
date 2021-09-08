import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from backend import BancoDeDados
from interfaces import (TelaDiretoriosBackup, TelaFiltrar, TelaLogin,
                        TelaPreferencias, TelaPrincipalAdmin,
                        TelaPrincipalCliente)
'''
Top1 = Toplevel(root, bg="light blue")
top1.geometry(str(scrW) + "x" + str(scrH))
top1.title("Top 1 Window")
top1.wm_attributes("-topmost", 1) ## Para que top1 esteja no topo no começo
'''
BANCO = "banco.db"
PREFERENCIAS = ".config.json"


class App():
    def __init__(self, master, banco):
        self.master = master
        self.master.withdraw()
        self.banco = BancoDeDados(banco)
        self.banco.exe_sql_file("backend/locadora.sql")
        self.usuario, tipo = self.login()
        if self.usuario == '':
            self.fechar()

        if tipo == "adm":
            self.telaprincipal = self.top(TelaPrincipalAdmin)
        else:
            self.telaprincipal = self.top(TelaPrincipalCliente)

    def top(self, tela, **kwargs):
        tp = tk.Toplevel(self.master)
        t = tela(tp, **kwargs)
        t.bind("<Escape>", self.fechar)
        return t

    def login(self):
        top = tk.Toplevel(self.master)
        tela = TelaLogin(top, self.banco)
        tela.bind("<Escape>", self.fechar)
        tela.wait_window()
        return tela.user

    def preferencias(self):
        print("Acessando preferencias")

    def fechar(self):
        self.master.destroy()
        self.banco.close()
        exit()


base = tk.Tk()
App(base, BANCO)
base.mainloop()
