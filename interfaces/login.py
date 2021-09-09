import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class TelaLogin(tk.Frame):
    def __init__(self, master, banco):
        tk.Frame.__init__(self, master)
        self.master = master
        self.bd = banco

        self.master.title("Login")

        self.container1 = tk.Frame(self.master, bd=5)
        self.container1.pack()

        tk.Label(self.container1, text="LOGAR USUÁRIO").pack(fill='x')

        self.container2 = tk.Frame(self.container1)
        self.container2.pack(fill='both', expand=1, padx=3, pady=3)

        tk.Label(self.container2, text="Login:").grid(column=0, row=0)
        self.login = tk.Entry(self.container2)
        self.login.grid(column=1, row=0)

        tk.Label(self.container2, text="Senha:").grid(column=0, row=1)
        self.senha = tk.Entry(self.container2)
        self.senha.grid(column=1, row=1)

        self.checkVar = tk.BooleanVar()

        tk.Checkbutton(self.container2,
                       text="Administrador",
                       variable=self.checkVar).grid(column=0,
                                                    row=2,
                                                    columnspan=2)

        self.btnLimpar = tk.Button(self.container1,
                                   text="LIMPAR",
                                   command=self.limpar_campos)
        self.btnLimpar.pack(side='left', fill='x', expand=1, padx=3)
        self.btnLogin = tk.Button(self.container1,
                                  text="LOGIN",
                                  command=self.logar_usuario)
        self.btnLogin.pack(side='left', fill='x', expand=1, padx=3)

        self.login.focus()

    def get_dados(self):
        return self.login.get().strip(), self.senha.get().strip()

    def limpar_campos(self):
        self.login.delete(0, tk.END)
        self.senha.delete(0, tk.END)
        self.login.focus()

    def verifica_campos(self):
        login, senha = self.get_dados()
        if login == '' or senha == '':
            messagebox.showinfo(
                "Aviso", "Preencha os campos login e senha para logar!")
            return False
        else:
            return True

    def logar_usuario(self):
        if self.verifica_campos():
            login, senha = self.get_dados()
            if self.checkVar.get():
                tabela = "admin"
            else:
                tabela = "cliente"
            res = self.bd.cursor.execute("SELECT login, senha FROM " +
                                         tabela).fetchall()
            usuarios = [x[0] for x in res]
            senhas = [x[1] for x in res]
            if login not in usuarios:
                messagebox.showwarning("Aviso",
                                       f"O login '{login}' não existe!")
            elif senhas[usuarios.index(login)] != senha:
                messagebox.showinfo("Aviso", "Senha incorreta!")
            else:
                return (login, tabela)
        return False


if __name__ == "__main__":
    bd = sqlite3.connect("teste.db")
    tela = tk.Tk()
    TelaLogin(tela, bd)
    tela.mainloop()
