import sqlite3


class BancoDeDados:
    def __init__(self):
        self._conexao = sqlite3.connect('locadora.db')
        self._cursor = self._conexao.cursor()

    def __enter__(self):
        return self

    @property
    def cursor(self):
        return self._cursor

    def sql(self, comando, valores=None):
        if valores == None:
            self.cursor.execute(comando)

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._conexao.close()