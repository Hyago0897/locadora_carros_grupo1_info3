import sqlite3
import re


class BancoDeDados:
    def __enter__(self):
        self._conexao = sqlite3.connect('locadora.db')
        self._cursor = self._conexao.cursor()
        return self

    @property
    def cursor(self):
        return self._cursor

    def exe_sql_file(self, filename):
        ###
        # Direitos para
        # nobeing -- no site -> ti-enxame.com
        ###
        command = ""
        for line in open(filename):
            if re.match(r'--', line):
                continue

            if not re.search(r'[^-;]+;', line):
                command += line
            else:
                command += line
                try:
                    self._cursor.execute(command)
                except (sqlite3.OperationalError, sqlite3.ProgrammingError) as e:
                    print("\n[WARN] MySQLError during execute statement \n\tArgs: '%s'" % (str(e.args)))

                command = ""


    def sql(self, comando, valores=None):
        if valores == None:
            self.cursor.execute(comando)

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._conexao.commit()
        self._conexao.close()
