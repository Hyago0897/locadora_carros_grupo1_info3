from tkinter import *
from tkinter import ttk
import sqlite3

#Classes:

class Conecta():
    def __init__(self):
        criaTabelaManutencao()
        try:
            self.conn = sqlite3.connect('bancoBagunca.db')
            self.cursor = self.conn.cursor()
        except:
            print('Erro ao se conectar com o banco de dados')
    def commit_db(self):
        if self.conn:
            self.conn.commit()
    def close_db(self):
        if self.conn:
            self.conn.close()

class tabelaManutencao():
    tabela = 'manutencao'
    def __init__(self):
        self.db = Conecta()
        self.tabela
    def consulta_dados(self):
        retorno = []
        self.db.cursor.execute("""
        SELECT *FROM manutencao;
        """)
        for registro in self.db.cursor.fetchall():
            retorno.append(registro)
        return retorno
    def desconectar(self):
        self.db.close_db()

def filtrarModelos():
    chamado = tabelaManutencao()
    modelos = str(chamado.consulta_dados())
    print(modelos)
    modelos = modelos.split('[')
    modelos = modelos[1].split(']')
    modelos = modelos[0].split('(')
    modelos01 = []
    cont = 0
    for i in modelos:
        if cont > 0:
            i = i.split(')')
            modelos01.append(i[0])
        cont += 1
    modelos = []
    for i in modelos01:
        i = i.split(',')
        i = i[0].split("'")
        modelos.append(i[1])

    return modelos

def inserirManutenção(modelo, custo_mm, descricao):
    modelo = str(modelo)
    custo_mm = str(custo_mm)
    descricao = str(descricao)

    conn = sqlite3.connect('bancoBagunca.db')

    cursor = conn.cursor()

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO manutencao
    VALUES (?,?,?);
    """, (modelo, custo_mm, descricao))

    conn.commit()

    conn.close()

def extraiDadosManutencao():
    chamado = tabelaManutencao()
    dados = str(chamado.consulta_dados())
    print(dados)
    return dados


'''tabelaManutencao()'''

'''inserirManutenção('Palio', 100, '')
inserirManutenção('Corsa', 150, '')
inserirManutenção('Coala', 120, '')
inserirManutenção('Chorola', 110, '')
inserirManutenção('Ferrari', 200, '')'''

'''print(filtrarModelos())'''