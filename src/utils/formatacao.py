
def formatar_cnpj(cnpj: str):
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

def formatar_valor_brasil(valor: float):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
