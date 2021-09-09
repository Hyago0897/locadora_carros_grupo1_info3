class TabelaManutencao():
    def __init__(self, database):
        self.db = database
    def consulta_dados(self):
        retorno = []
        result = self.db.exe("""
        SELECT *FROM manutencao;
        """)
        for registro in result.fetchall():
            retorno.append(registro)
        return retorno

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

def extrai_dados_manutencao(database):
    chamado = TabelaManutencao(database)
    dados = str(chamado.consulta_dados())
    print(dados)
    return dados
