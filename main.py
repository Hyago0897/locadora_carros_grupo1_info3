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


class App():
    def __init__(self, master, banco):
        self.master = master
        self.master.withdraw()
        self.banco = BancoDeDados(BANCO)
        self.usuario = self.login()

    def login(self):
        top = tk.Toplevel(self.master)
        top.protocol("WM_DELETE_WINDOW", self.fechar)
        tela = TelaLogin(top, self.banco)
        tela.bind("<Escape>", self.fechar)

    def fechar(self):
        if messagebox.askokcancel("Sair", "Deseja fechar o programa?"):
            self.master.destroy()


base = tk.Tk()
App(base, BANCO)
base.mainloop()
