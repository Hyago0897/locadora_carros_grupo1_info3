import tkinter as tk
from tkinter.constants import N
import interfaces


class Janela(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._tela = None
        self.mudaTela(interfaces.TelaLogin)

    def mudaTela(self, tela):
        nova_tela = tela(self)
        if self._tela is not None:
            self._tela.destroy()
        self._tela = nova_tela
        self._tela.pack()

if __name__ == "__main__":
    app = Janela()
    app.mainloop()

'''
top1 = Toplevel(root, bg="light blue")
top1.geometry(str(scrW) + "x" + str(scrH))
top1.title("Top 1 Window")
top1.wm_attributes("-topmost", 1) ## Para que top1 esteja no topo no começo
'''
