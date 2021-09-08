import json
import schedule, time, shutil, zipfile
from datetime import datetime


ARQUIVO = "locals_backup.json"


class Backup:
    def __inti__(self):
        self.config = ConfigurationBackup()

    def configura_local(self, lista):
        self.config.mudar_local = lista

    def configura_tempo(self, tempo):
        self.config.mudar_tempo = tempo
    
    def executar_backup(self):
        nome = "locadora"
        data = datetime.now()
        data = data.strftime("%d%m%Y%H%M%S")
        shutil.make_archive(f'{nome+data}', 'zip', '../teste', 'file1.txt')


class ConfigurationBackup:
    def __init__(self):
        dict_create = {
            "locals": [],
            "tempo": 1
        }
        self.arq_json = None
        self.arq_json = self.abri_json('r', dict_create)
        if self.arq_json is not None: self.locais = self.locais_backups(self.arq_json["locals"])
        self.tempo = self.arq_json["tempo"]

    def abri_json(self, abertura, valores):
        try:
            if abertura == 'r':
                with open(ARQUIVO, abertura, encoding="utf-8") as arq:
                    return json.load(arq)
            else:
                with open(ARQUIVO, abertura, encoding="utf-8") as arq:
                    json.dump(valores, arq, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

        except FileNotFoundError:
            with open(ARQUIVO, 'a', encoding="utf-8") as arq:
                json.dump(valores, arq, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

    @staticmethod
    def locais_backups(locals):
        lista = []
        for l in locals:
            lista.append(l)
        return lista

    @property
    def locais(self):
        return self._locais

    @locais.setter
    def locais(self, value):
        self._locais = value

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        self._tempo = tempo

    def mudar_local(self, novo_local):
        if not self.arq_json:
            return False
        
        self.locais = novo_local
        self.arq_json["locals"] = self.locais
        self.abri_json('w', self.arq_json)

    def mudar_tempo(self, novo_tempo):
        if not self.arq_json:
            return False

        self.arq_json['tempo'] = novo_tempo
