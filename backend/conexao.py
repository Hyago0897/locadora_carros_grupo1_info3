import re
import sqlite3


class BancoDeDados:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except Exception:
            print('Erro ao se conectar com o banco de dados')

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
                    self.cursor.execute(command)
                except (sqlite3.OperationalError,
                        sqlite3.ProgrammingError) as e:
                    return False

                command = ""

    def exe(self, sql: str):
        resultado = self.cursor.execute(sql)
        self.commit_db()
        return resultado

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
