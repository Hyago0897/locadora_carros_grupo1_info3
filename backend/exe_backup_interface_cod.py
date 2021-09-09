import threading, time, schedule
import tkinter as tk


class ExeTarefas(threading.Thread):
    def __init__(self, tarefa):
        threading.Thread.__init__(self, target=tarefa)
        self.tarefa = tarefa

    @property
    def tarefa(self): return self._tarefa
    @tarefa.setter
    def tarefa(self, value): self._tarefa = value
