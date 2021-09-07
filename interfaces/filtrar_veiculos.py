import tkinter as tk
import tkinter.ttk as ttk


class TelaFiltrar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("FILTRAR")

        self.container1 = tk.Frame(master)
        self.container1.pack(fill="both", expand=1)

        self.container2 = tk.Frame(self.container1)
        self.container2.pack(fill="y", expand=1, padx=3, pady=3)

        self.btnOk = tk.Button(self.container1, text="OK \N{CHECK MARK}")
        self.btnOk.pack(side="bottom", anchor="e", padx=6, pady=6)

        self.checkVar_modelo = tk.BooleanVar()
        self.checkVar_marca = tk.BooleanVar()
        self.checkVar_cor = tk.BooleanVar()

        tk.Checkbutton(self.container2,
                       text="Modelo",
                       variable=self.checkVar_modelo,
                       command=self.filtra_modelo).grid(column=0,
                                                        row=0,
                                                        padx=3,
                                                        pady=3,
                                                        sticky="w")

        self.modelo = ttk.Combobox(self.container2, state="readonly")
        self.modelo.grid(column=0, row=1, padx=(15, 5), sticky="w")

        tk.Checkbutton(self.container2,
                       text="Marca",
                       variable=self.checkVar_marca,
                       command=self.filtra_marca).grid(column=0,
                                                       row=2,
                                                       padx=3,
                                                       pady=3,
                                                       sticky="w")

        self.marca = ttk.Combobox(self.container2, state="readonly")
        self.marca.grid(column=0, row=3, padx=(15, 5), sticky="w")

        tk.Checkbutton(self.container2,
                       text="Cor",
                       variable=self.checkVar_cor,
                       command=self.filtra_cor).grid(column=0,
                                                     row=4,
                                                     padx=3,
                                                     pady=3,
                                                     sticky="w")

        self.cor = ttk.Combobox(self.container2, state="readonly")
        self.cor.grid(column=0, row=5, padx=(15, 5), sticky="w")

        self.filtra_modelo()
        self.filtra_marca()
        self.filtra_cor()

    def filtra_modelo(self):
        if self.checkVar_modelo.get():
            self.modelo.configure(state="readonly")
        else:
            self.modelo.configure(state="disabled")

    def filtra_marca(self):
        if self.checkVar_marca.get():
            self.marca.configure(state="readonly")
        else:
            self.marca.configure(state="disabled")

    def filtra_cor(self):
        if self.checkVar_cor.get():
            self.cor.configure(state="readonly")
        else:
            self.cor.configure(state="disabled")


if __name__ == "__main__":
    tela = tk.Tk()
    TelaFiltrar(tela)
    tela.mainloop()
