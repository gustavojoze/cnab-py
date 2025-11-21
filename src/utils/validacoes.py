
# coloquei o tamanho maximo de 400 caracteres, porque o cnab400 tem 
# esse tamanho maximo

def linha_valida(linha: str):
    linha = linha.strip()
    if not linha:
        return False
    TAMANHO_MAXIMO = 400
    if len(linha) > TAMANHO_MAXIMO:
        return False
    return True


from datetime import datetime


def validar_cnpj(cnpj: str, numero_linha: int):
    if cnpj.isdigit() and len(cnpj) == 14:
        return None  # válido
    return f"CNPJ contém caracteres inválidos - linha {numero_linha}"


def validar_data(data: str, numero_linha: int):
    if len(data) == 8 and data.isdigit():
        try:
            return datetime.strptime(data, "%Y%m%d").strftime("%d/%m/%Y")
        except ValueError:
            pass
    return f"Data inválida - linha {numero_linha}"


def validar_valor(valor: str, numero_linha: int):
    if valor.isdigit():
        return float(int(valor)) / 100
    return f"Valor contém caracteres inválidos - linha {numero_linha}"


def validacoes(cnpj, valor):
    if len(cnpj) != 14 or not cnpj.isdigit():
        return "rejeitado"

    if valor <= 0:
        return "rejeitado"

    if valor <= 10000:
        return "aprovado"

    if 10001 <= valor <= 50000:
        return "pendente_validacao"

    return "rejeitado"

