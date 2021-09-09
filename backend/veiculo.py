class TabelaVeiculo():
    def __init__(self, database):
        self.db = database
    def consulta_dados(self):
        retorno = []
        result = self.db.exe("""
        SELECT *FROM veiculo;
        """)
        for registro in result.fetchall():
            retorno.append(registro)
        return retorno


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

def filtrar_veiculos(database, modelo, marca, cor):
    dadosBase = formatar_veiculos(database)
    for campo, valor in ((modelo, marca, cor), (3, 2, 4)):
        if campo == None or campo == '':
            pass
        else:
            tabela_aux = []
            for i in range(len(dadosBase)):
                a = dadosBase[i][valor]
                if a == campo:
                    tabela_aux.append(dadosBase[i])
            dadosBase = tabela_aux

    for i in range(len(dadosBase)):
        print(dadosBase[i])
