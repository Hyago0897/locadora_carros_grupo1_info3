import sqlite3

#Classes:

#class Conecta():
    #def __init__(self, data_base):
    #    try:
    #        self.conn = sqlite3.connect(data_base)
    #        self.cursor = self.conn.cursor()
    #    except:
    #        print('Erro ao se conectar com o banco de dados')
    #def commit_db(self):
    #    if self.conn:
    #        self.conn.commit()
    #def close_db(self):
    #    if self.conn:
    #        self.conn.close()

class TabelaVeiculo():
    def __init__(self, database):
        self.db = database
        self.tabela
    def consulta_dados(self):
        retorno = []
        result = self.db.exe("""
        SELECT *FROM veiculo;
        """)
        for registro in result.fetchall():
            retorno.append(registro)
        return retorno
    #def desconectar(self):
    #    self.db.close_db()

#Funções:

#def inserir_veiculo(placa, marca, modelo, cor, descricao, ano, status_veiculo):
    #placa = str(placa)
    #marca = str(marca)
    #modelo = str(modelo)
    #cor = str(cor)
    #descricao = str(descricao)
    #ano = str(ano)
    #status_veiculo = str(status_veiculo)

    #conn = sqlite3.connect('bancoBagunca.db')

    #cursor = conn.cursor()

    # inserindo dados na tabela
    #cursor.execute("""
    #INSERT INTO veiculo (placa, marca, modelo, cor, descricao, ano, status_veiculo)
    #VALUES (?,?,?,?,?,?,?);
    #""", (placa, marca, modelo, cor, descricao, ano, status_veiculo))

    #conn.commit()

    #conn.close()

def extrai_dados_veiculo(database):
    chamado = TabelaVeiculo(database)
    dados = str(chamado.consulta_dados())
    return dados

def formatar_veiculos(database):
    tabelaRetorno = []
    dadosBase_b = []
    dadosBase = extrai_dados_veiculo(database)
    dadosBase = dadosBase.split(',')
    for i in range(len(dadosBase)):
        p = str(i/8)
        p = p.split('.')
        q = str((i + 1) / 8)
        q = q.split('.')
        if p[1] == '0':
            dado = dadosBase[i].split('(')
            dadosBase_b.append(dado[1])

        elif q[1] == '0' and q[0] != '0':
            aux = dadosBase[i].split(')')
            aux = aux[0].split("'")
            dadosBase_b.append(aux[1])
            tabelaRetorno.append(dadosBase_b)
            dadosBase_b = []
        else:
            aux = dadosBase[i].split("'")
            dadosBase_b.append(aux[1])
    return tabelaRetorno

def filtrar_veiculos(modelo, marca, cor):
    dadosBase = formatar_veiculos()
    if modelo == None or modelo == '':
        pass
    else:
        tabela_aux = []
        for i in range(len(dadosBase)):
            a = dadosBase[i][3]
            if a == modelo:
                tabela_aux.append(dadosBase[i])
        dadosBase = tabela_aux

    if marca == None or marca == '':
        pass
    else:
        tabela_aux = []
        for i in range(len(dadosBase)):
            a = dadosBase[i][2]
            if a == marca:
                tabela_aux.append(dadosBase[i])
        dadosBase = tabela_aux
    if cor == None or cor == '':
        pass
    else:
        tabela_aux = []
        for i in range(len(dadosBase)):
            a = dadosBase[i][4]
            if a == cor:
                tabela_aux.append(dadosBase[i])
        dadosBase = tabela_aux
    for i in range(len(dadosBase)):
        print(dadosBase[i])

