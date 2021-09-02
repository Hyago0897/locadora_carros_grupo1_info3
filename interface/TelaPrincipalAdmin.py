import tkinter as tk
import tkinter.ttk as ttk


class TelaPrincipalAdmin(tk.Toplevel):
    def __init__(self, master, admin):
        self.master = master
        self.admin = admin

        self.container1 = tk.Frame(self.master)
        self.container1.pack(fill="both", expand=1)

        self.abas = ttk.Notebook(self.container1)
        self.abas.pack(fill="both", expand=1)

        self.painel1 = tk.Frame(self.abas)
        self.painel2 = tk.Frame(self.abas)
        self.painel3 = tk.Frame(self.abas)

        self.painel1.pack(fill="both", expand=1)
        self.painel2.pack(fill="both", expand=1)
        self.painel3.pack(fill="both", expand=1)

        self.abas.add(self.painel1, text="Primeiro")
        self.abas.add(self.painel2, text="Segundo")
        self.abas.add(self.painel3, text="Terceiro")

        tk.Label(self.painel1, text="Testando aqui 1!").pack(fill="both", expand=1)


if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("300x200")
    TelaPrincipalAdmin(app, '')
    app.mainloop()
