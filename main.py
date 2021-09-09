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

        self.topLogin = tk.Toplevel(self.master)
        self.topTPAdmin = tk.Toplevel(self.master)
        self.topTPCliente = tk.Toplevel(self.master)
        self.topPref = tk.Toplevel(self.topTPAdmin)
        self.topFiltro = tk.Toplevel(self.topTPCliente)
        self.topBk = tk.Toplevel(self.topPref)

        self.topTPAdmin.withdraw()
        self.topTPCliente.withdraw()
        self.topPref.withdraw()
        self.topFiltro.withdraw()
        self.topBk.withdraw()

        self.topTPAdmin.protocol("WM_DELETE_WINDOW", self.fechar)
        self.topTPCliente.protocol("WM_DELETE_WINDOW", self.fechar)
        self.topLogin.protocol("WM_DELETE_WINDOW", self.fechar)

        self.topPref.protocol("WM_DELETE_WINDOW", self.fechar_pref)

        self.admin = TelaPrincipalAdmin(self.topTPAdmin)
        self.admin.prog.entryconfigure(0, command=self.abrir_pref)
        self.admin.prog.entryconfigure(1, command=self.fechar)

        self.cliente = TelaPrincipalCliente(self.topTPCliente)
        self.pref = TelaPreferencias(self.topPref, PREFERENCIAS)
        self.filtro = TelaFiltrar(self.topFiltro)
        self.bk = TelaDiretoriosBackup(self.topBk)
        self.login = TelaLogin(self.topLogin, self.banco)

        self.login.btnLogin.configure(command=self.logar)

    def logar(self):
        usuario = self.login.logar_usuario()
        if usuario:
            self.topLogin.withdraw()
            self.login.limpar_campos()
            if usuario[1] == "admin":
                self.topTPAdmin.deiconify()
                self.admin.renomear(usuario[0])

    def abrir_pref(self):
        self.topPref.deiconify()
        self.topPref.grab_set()

    def fechar_pref(self):
        self.topPref.grab_release()
        self.topPref.withdraw()

    def fechar(self):
        self.master.destroy()
        self.banco.close()
        exit()


base = tk.Tk()
App(base, BANCO)
base.mainloop()
