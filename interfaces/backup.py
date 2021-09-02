import tkinter as tk
import tkinter.ttk as ttk


class TelaBackup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        master.title("BACKUP")

        self.container1 = tk.Frame(master)
        self.container1.pack(fill="both", expand=1)

        tk.Label(self.container1, text="Diretórios para Backup").pack(fill="x")

        self.container2 = tk.Frame(self.container1)
        self.container2.pack(fill="both", expand=1)

        self.container3 = tk.Frame(self.container2)
        self.container3.grid(column=0, row=0, rowspan=4)

        self.container4 = tk.Frame(self.container2)
        self.container4.grid(column=1, row=0, rowspan=3)

        barraV = ttk.Scrollbar(self.container3, orient="vertical")
        barraH = ttk.Scrollbar(self.container3, orient="horizontal")
        self.lista_clientes = tk.Listbox(self.container3,
                                         width=20,
                                         height=7,
                                         yscrollcommand=barraV.set,
                                         xscrollcommand=barraH.set,
                                         selectmode=tk.SINGLE)
        barraV.config(command=self.lista_clientes.yview)
        barraV.pack(side="right", fill='y')
        barraH.config(command=self.lista_clientes.xview)
        barraH.pack(side="bottom", fill='x')

        self.lista_clientes.pack(fill='x')

        tk.Button(self.container4, text="ADICIONAR").pack(fill="both",
                                                          expand=1,
                                                          pady=(0, 2),
                                                          padx=(3, 3))
        tk.Button(self.container4, text="EDITAR").pack(fill="both",
                                                       expand=1,
                                                       pady=(0, 2),
                                                       padx=(3, 3))
        tk.Button(self.container4, text="DELETAR").pack(fill="both",
                                                        expand=1,
                                                        pady=(0, 0),
                                                        padx=(3, 3))

        tk.Button(self.container2, text="SALVAR").grid(column=1, row=3)


if __name__ == "__main__":
    app = tk.Tk()
    TelaBackup(app)
    app.mainloop()
