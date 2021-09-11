import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring

from backend import BancoDeDados
from interfaces import (TelaDiretoriosBackup, TelaFiltrar, TelaLogin,
                        TelaPreferencias, TelaPrincipalAdmin,
                        TelaPrincipalCliente)

BANCO = "banco.db"
PREFERENCIAS = ".config.json"


class App():
    def __init__(self, master, banco):
        self.master = master
        self.master.withdraw()
        if not os.path.isfile(banco):
            self.banco = BancoDeDados(banco)
            self.banco.exe_sql_file("backend/locadora.sql")
        else:
            self.banco = BancoDeDados(banco)
        self.verifica_admin()

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

        # LOGIN
        self.topLogin.protocol("WM_DELETE_WINDOW", self.fechar)
        self.login = TelaLogin(self.topLogin, self.banco)
        self.login.btnLogin.configure(command=self.logar)

        # ADMIN
        self.topTPAdmin.protocol("WM_DELETE_WINDOW", self.fechar)
        self.admin = TelaPrincipalAdmin(self.topTPAdmin, banco=self.banco)
        self.admin.prog.entryconfigure(0, command=self.abrir_pref)
        self.admin.prog.entryconfigure(1, command=self.fechar)
        self.admin.logout.configure(command=self.logoutAdm)

        # CLIENTE
        self.topTPCliente.protocol("WM_DELETE_WINDOW", self.fechar)
        self.cliente = TelaPrincipalCliente(self.topTPCliente,
                                            banco=self.banco)
        self.cliente.filtro.configure(command=self.abrir_filtro)
        self.cliente.logout.configure(command=self.logoutCliente)

        # PREFERENCIAS
        self.topPref.protocol("WM_DELETE_WINDOW", self.fechar_pref)
        self.pref = TelaPreferencias(self.topPref, PREFERENCIAS)
        self.pref.btnOk.configure(command=self.prefok)
        self.pref.btn_preferencias.configure(command=self.abrir_dirbk)
        self.pref.btn_importar.configure(command=self.importar_banco)

        # DIRBACKUP
        self.topBk.protocol("WM_DELETE_WINDOW", self.fechar_dirbk)
        self.bk = TelaDiretoriosBackup(self.topBk)
        self.bk.btn_salvar.configure(command=self.dirbkok)

        # FILTRO
        self.topFiltro.protocol("WM_DELETE_WINDOW", self.fechar_filtro)
        self.filtro = TelaFiltrar(self.topFiltro)
        self.filtro.btnOk.configure(command=self.filtroOk)

    def verifica_admin(self):
        quant_adms = len(self.banco.exe("SELECT * FROM ADMIN").fetchall())
        if not quant_adms:
            if messagebox.askyesno(
                    title="Criar admin",
                    message="Nenhum admin foi encontrado, deseja criar?"):
                while True:
                    nome = askstring("Dados admin", "Nome do admin:")
                    login = askstring("Dados admin", "Login do admin:")
                    senha = askstring("Dados admin",
                                      "Senha do admin:",
                                      show='*')

                    if nome and login and senha:
                        self.banco.exe(f"""INSERT INTO ADMIN(login, senha,nome)
                            VALUES ('{login}','{senha}','{nome}');""")
                        break
                    else:
                        if not messagebox.askokcancel(
                                title="Aviso",
                                message="Preencha todos os campos!\n"
                                "Deseja tentar novamente?"):
                            break

    def logar(self):
        usuario = self.login.logar_usuario()
        if usuario:
            self.topLogin.withdraw()
            self.login.limpar_campos()
            if usuario[1] == "admin":
                self.topTPAdmin.deiconify()
                self.admin.renomear(usuario[0])
            else:
                self.topTPCliente.deiconify()
                self.cliente.renomear(usuario[0])

    def logoutAdm(self):
        self.topTPAdmin.withdraw()
        self.topLogin.deiconify()

    def logoutCliente(self):
        self.topTPCliente.withdraw()
        self.topLogin.deiconify()

    def abrir_pref(self):
        self.topPref.deiconify()
        self.topPref.grab_set()

    def fechar_pref(self):
        self.topPref.grab_release()
        self.topPref.withdraw()

    def prefok(self):
        self.topPref.grab_release()
        self.topPref.withdraw()

    def abrir_dirbk(self):
        self.topBk.deiconify()
        self.topBk.grab_set()

    def fechar_dirbk(self):
        self.topBk.grab_release()
        self.topBk.withdraw()

    def dirbkok(self):
        self.topBk.grab_release()
        self.topBk.withdraw()

    def abrir_filtro(self):
        self.topFiltro.deiconify()
        self.topFiltro.grab_set()

    def fechar_filtro(self):
        self.topFiltro.grab_release()
        self.topFiltro.withdraw()

    def filtroOk(self):
        self.topFiltro.grab_release()
        self.topFiltro.withdraw()

    def fechar(self):
        self.master.destroy()
        self.banco.close()
        exit()

    def importar_banco(self):
        pass


base = tk.Tk()
App(base, BANCO)
base.mainloop()
