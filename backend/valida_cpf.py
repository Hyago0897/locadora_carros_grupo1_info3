import re


class ValidaCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = re.sub(r'[^0-9]', '',cpf)

    def valida(self):
        if not self.cpf:
            return False

        novo_cpf = self._calcula_digito(self.cpf[:9])
        novo_cpf = self._calcula_digito(novo_cpf)
        
        if novo_cpf == self.cpf:
            return True
        return False

    @staticmethod
    def _calcula_digito(fatia_cpf):
        if not fatia_cpf:
            return False

        sequencia = fatia_cpf[0] * len(fatia_cpf)
        if sequencia == fatia_cpf:
            return False
        soma = 0
        for chave, multi in enumerate(range(len(fatia_cpf)+1, 1, -1)):
            soma += int(fatia_cpf[chave]) * multi
        digito = 11 - (soma%11)
        if digito >= 10:
            return (fatia_cpf + str(0))
        return (fatia_cpf + str(digito))

if __name__ == "__main__":
    cpf = '123.456.789-09'
    a = ValidaCPF(cpf)
    a.valida()