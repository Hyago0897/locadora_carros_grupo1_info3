import tkinter as tk
import tkinter.ttk as ttk


class TelaPreferencias(tk.Frame):
    def __init__(self, master, arq_preferencias):
        tk.Frame.__init__(self, master)
        self.arq = arq_preferencias
        master.title("PREFERÊNCIAS")

        self.container1 = tk.Frame(master)
        self.container1.pack(fill="both", expand=1)

        self.container2 = tk.Frame(self.container1)
        self.container2.pack(fill="y", expand=1, padx=3, pady=3)

        self.btnOk = tk.Button(self.container1, text="OK \N{CHECK MARK}")
        self.btnOk.pack(side="bottom", anchor="e", padx=6, pady=6)

        self.checkVar = tk.IntVar()
        self.check_backup = tk.Checkbutton(self.container2,
                                           text="Fazer backup",
                                           variable=self.checkVar,
                                           command=self.habilita_backup)
        self.check_backup.grid(column=0, row=0, sticky="w")

        self.lbdir = tk.Label(self.container2, text="Diretórios para backup")
        self.lbdir.grid(column=0, row=1, padx=(20, 0), sticky="w")

        self.btn_preferencias = tk.Button(self.container2, text="...")

        self.btn_preferencias.grid(column=1, row=1, padx=1, pady=1)

        self.lbinter = tk.Label(self.container2,
                                text="Intervalo para backup (min)")
        self.lbinter.grid(column=0, row=2, padx=(20, 0), sticky="w")

        self.tempo_backup = ttk.Spinbox(self.container2,
                                        from_=1,
                                        to=60,
                                        increment=1,
                                        width=2,
                                        state="readonly")
        self.tempo_backup.grid(column=1, row=2, sticky="w", padx=2, pady=2)
        self.tempo_backup.set(1)
        self.habilita_backup()
        tk.Label(self.container2,
                 text="Importar arquivo de backup").grid(column=0,
                                                         row=3,
                                                         sticky="w",
                                                         padx=(8, 2),
                                                         pady=6)
        self.btn_importar = tk.Button(self.container2, text="...")

        self.btn_importar.grid(column=1, row=3, padx=2, pady=2, sticky="w")

    def habilita_backup(self):
        status = bool(self.checkVar.get())

        if status:
            self.btn_preferencias.configure(state="normal")
            self.tempo_backup.configure(state="readonly")
            self.lbdir.configure(state="normal")
            self.lbinter.configure(state="normal")

        else:
            self.btn_preferencias.configure(state="disabled")
            self.tempo_backup.configure(state="disabled")
            self.lbdir.configure(state="disabled")
            self.lbinter.configure(state="disabled")


if __name__ == "__main__":
    tela = tk.Tk()
    TelaPreferencias(tela, '')
    tela.mainloop()
