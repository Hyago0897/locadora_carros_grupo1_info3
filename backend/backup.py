import json
import os, shutil
from datetime import datetime


class ConfigurationBackup:
    def __init__(self, file_name):
        self.file_name = file_name
        dict_create = {"locals": [],"tempo": 1}
        self.arq_json = None
        self.arq_json = self.abri_json('r', dict_create)
        if self.arq_json is not None: self.locais, self.tempo = self._locais_backups_(self.arq_json["locals"]), self.arq_json["tempo"]

    def abri_json(self, abertura, valores):
        try:
            if abertura == 'r':
                with open(self.file_name, abertura, encoding="utf-8") as arq:
                    return json.load(arq)
            else:
                with open(self.file_name, abertura, encoding="utf-8") as arq:
                    json.dump(valores, arq, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

        except FileNotFoundError:
            with open(self.file_name, 'a', encoding="utf-8") as arq:
                json.dump(valores, arq, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

    @staticmethod
    def _locais_backups_(locals):
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
        self.abri_json('w', self.arq_json)


class Backup(ConfigurationBackup):
    def __init__(self, file_config):
        ConfigurationBackup.__init__(self, file_config)
    
    def executar_backup(self, name_db):
        nome = name_db
        data = datetime.now()
        data_formatada = data.strftime("%d%m%Y%H%M%S")
        nome = nome+data_formatada
        origem_bkp = shutil.make_archive(f'{nome}', 'zip', './', name_db)
        self.mover_para(origem_bkp)
    
    def mover_para(self, origem_bkp):
        if self.locais != '':
            for c in self.locais:
                shutil.copy(origem_bkp, c)
            os.remove(origem_bkp)
