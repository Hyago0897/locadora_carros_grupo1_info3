import re


def valida_email(email):
    regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    res = regex.match(email)
    return email == '' or res is not None


def valida_valor(valor):
    regex = re.compile(r"\d+(\.\d{,2})?$")
    res = regex.match(valor)
    return valor == '' or res is not None
