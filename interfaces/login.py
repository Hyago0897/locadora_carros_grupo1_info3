import tkinter as tk
import tkinter.ttk as ttk



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
        self.nome = tk.Entry(self.container2)
        self.nome.grid(column=1, row=0)

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
                                  command=self.verificar_dados)
        self.btnLogin.pack(side='left', fill='x', expand=1, padx=3)

        self.nome.focus()

    def limpar_campos(self):
        self.nome.delete(0, tk.END)
        self.senha.delete(0, tk.END)
        self.nome.focus()

    def verificar_dados(self):
        print(self.nome.get() == "gilson")
        return self.nome.get() == "gilson"


if __name__ == "__main__":
    tela = tk.Tk()
    TelaLogin(tela, '')
    tela.mainloop()
