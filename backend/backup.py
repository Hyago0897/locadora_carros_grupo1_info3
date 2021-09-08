import json


ARQUIVO = "locals_backup.json"


class ConfigurationBackup:
    def __init__(self):
        dict_create = {
            "locals": [],
            "tempo": 1
        }
        self.arq_json = None
        self.arq_json = self.abri_json('r', dict_create)
        self.locais = self.locais_backups(self.arq_json["locals"])

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
