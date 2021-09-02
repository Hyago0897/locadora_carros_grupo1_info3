import tkinter as tk
from tkinter.constants import LEFT
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
        self.check_backup = tk.Checkbutton(
            self.container2, text="Fazer backup", variable=self.checkVar, command=self.habilita_backup).grid(column=0, row=0, sticky="w")

        tk.Label(self.container2, text="Diretórios para backup").grid(
            column=0, row=1, padx=(20, 0), sticky="w")

        self.btn_preferencias = tk.Button(self.container2, text="...")
        self.btn_preferencias.grid(column=1, row=1, padx=1, pady=1)

        tk.Label(self.container2, text="Intervalo para backup").grid(
            column=0, row=2, padx=(20, 0), sticky="w")

        self.tempo_backup = ttk.Spinbox(
            self.container2, from_=1, to=60, increment=1, width=2, state="readonly")
        self.tempo_backup.grid(column=1, row=2, sticky="w", padx=2, pady=2)
        self.tempo_backup.set(1)
        self.habilita_backup()

    def habilita_backup(self):
        status = bool(self.checkVar.get())

        if status:
            self.btn_preferencias.configure(state="normal")
            self.tempo_backup.configure(state="readonly")
        else:
            self.btn_preferencias.configure(state="disabled")
            self.tempo_backup.configure(state="disabled")


if __name__ == "__main__":
    tela = tk.Tk()
    TelaPreferencias(tela, '')
    tela.mainloop()
