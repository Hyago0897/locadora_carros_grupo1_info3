import tkinter as tk
import re


class SimpleDateEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, mst, **kwargs)

        self.bind("<KeyPress>", self.__inserir)
        self.bind("<KeyRelease>", self.__inserir)
        self.bind("<FocusIn>", self.__cursor)
        self.bind("<ButtonRelease>", self.__cursor)
        self.cursorpos = 0

    def __cursor(self, e):
        self.icursor(self.cursorpos)

    def __inserir(self, e):
        if e.keysym in "0123456789":
            if len(self.get()) == 2:
                if self.get()[:2] > "31":
                    self.delete(0, tk.END)
                    self.insert(tk.END, "31")
                elif self.get()[:2] == "00":
                    self.delete(0, tk.END)
                    self.insert(0, "01")
                self.insert(tk.END, "/")

            elif len(self.get()) == 5:
                if self.get()[3:5] > "12":
                    self.delete(3, tk.END)
                    self.insert(tk.END, "12")
                elif self.get()[3:5] in ("04", "06", "09",
                                         "11") and self.get()[:2] == "31":
                    self.delete(1)
                    self.insert(1, "0")
                elif self.get()[3:5] == "02":
                    if self.get()[:2] > "29":
                        self.delete(0, 2)
                        self.insert(0, "29")
                elif self.get()[3:5] == "00":
                    self.delete(3, tk.END)
                    self.insert(tk.END, "01")

                self.insert(tk.END, "/")

            elif len(self.get()) >= 10:
                if self.get()[6:10] < "2000":
                    self.delete(6, tk.END)
                    self.insert(6, "2000")
                if self.get()[3:5] == "02":
                    if SimpleDateEntry.ehbissexto(int(self.get()[6:10])):
                        dm = "29"
                    else:
                        dm = "28"

                    if self.get()[:2] > dm:
                        self.delete(0, 2)
                        self.insert(0, dm)

                self.delete(10, tk.END)
            self.cursorpos = self.index(tk.INSERT)
        elif e.keysym == "BackSpace":
            self.delete(tk.END)
            self.cursorpos = self.index(tk.INSERT)
        elif e.keysym in ("Tab", "ISO_Left_Tab"):
            self.select_clear()
        else:
            return "break"


class PlacaEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, master=mst, **kwargs)

        self.bind("<KeyPress>", self.__inserir)
        self.bind("<KeyRelease>", self.__inserir)
        self.bind("<FocusIn>", self.__cursor)
        self.bind("<ButtonRelease>", self.__cursor)
        self.regexletra = re.compile(r'^[A-Z]$')
        self.regexnum = re.compile(r'^[0-9]$')
        self.cursorpos = 0

    def __cursor(self, e):
        self.icursor(self.cursorpos)

    def __inserir(self, e):
        if self.regexletra.match(e.keysym.upper()) or self.regexnum.match(e.keysym.upper()):
            text = self.get().upper()
            self.delete(0, tk.END)
            self.insert(0, text)
            if len(self.get()) < 3:
                if not self.regexletra.match(e.keysym.upper()):
                    return "break"
            elif len(self.get()) <= 7:
                if not self.regexnum.match(e.keysym.upper()):
                    return "break"
            elif len(self.get()) > 7:
                self.delete(7, tk.END)

        elif e.keysym == "BackSpace":
            self.delete(tk.END)
        elif e.keysym in ("Tab", "ISO_Left_Tab"):
            self.select_clear()
        else:
            return "break"


class CPFEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, mst, **kwargs)


class EmailEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, mst, **kwargs)


class FoneEntry(tk.Entry):
    def __init__(self, mst, **kwargs):
        tk.Entry.__init__(self, mst, **kwargs)
