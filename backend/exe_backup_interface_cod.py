import threading, time, schedule
import tkinter as tk


class ExeTarefas(threading.Thread):
    def __init__(self, tarefa):
        threading.Thread.__init__(self, target=tarefa)
