import re
import sqlite3


class BancoDeDados:
    def __enter__(self):
        self._conexao = sqlite3.connect('back_end/bancoDados/locadora.db')
        self._cursor = self._conexao.cursor()
        self.exe_sql_file('back_end/bancoDados/locadora.sql')
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
                except (sqlite3.OperationalError,
                        sqlite3.ProgrammingError) as e:
                    print(
                        "\n[WARN] MySQLError during execute statement \n\tArgs: '%s'"
                        % (str(e.args)))

                command = ""

        print('terminou sem erro')

    def sql(self, comando, valores=None):
        if valores == None:
            self.cursor.execute(comando)

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._conexao.commit()
        self._conexao.close()


if __name__ == "__main__":
    with BancoDeDados() as a:
        print('a')