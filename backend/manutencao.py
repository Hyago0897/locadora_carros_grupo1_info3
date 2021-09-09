from tkinter import *
from tkinter import ttk
import sqlite3

#Classes:

#class Conecta():
#    def __init__(self, data_base):
#        try:
#            self.conn = sqlite3.connect(data_base)
#            self.cursor = self.conn.cursor()
#        except:
#            print('Erro ao se conectar com o banco de dados')
#    def commit_db(self):
#        if self.conn:
#            self.conn.commit()
#    def close_db(self):
#        if self.conn:
#            self.conn.close()

class TabelaManutencao():
    def __init__(self, database):
        self.db = database
        self.tabela
    def consulta_dados(self):
        retorno = []
        result = self.db.exe("""
        SELECT *FROM manutencao;
        """)
        for registro in result.fetchall():
            retorno.append(registro)
        return retorno
    #def desconectar(self):
    #    self.db.close_db()

def filtrar_modelos(database):
    chamado = TabelaManutencao(database)
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

#def inserir_manutencao(modelo, custo_mm, descricao):
#    modelo = str(modelo)
#    custo_mm = str(custo_mm)
#    descricao = str(descricao)

#    conn = sqlite3.connect('bancoBagunca.db')

#    cursor = conn.cursor()

    # inserindo dados na tabela
#    cursor.execute("""
#    INSERT INTO manutencao
#    VALUES (?,?,?);
#    """, (modelo, custo_mm, descricao))

#    conn.commit()

#    conn.close()

def extrai_dados_manutencao(database):
    chamado = TabelaManutencao(database)
    dados = str(chamado.consulta_dados())
    print(dados)
    return dados
