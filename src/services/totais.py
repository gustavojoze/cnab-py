
# 5 Questões:
# a) Como você lidaria com uma linha de detalhe com valor inválido (por exemplo, letras no campo numérico)?
# Coloquei uma verificação para identificar valores inválidos e registrar um erro específico para essas linhas,
# permitindo que o processamento continue para as outras linhas válidas.
# b) Como você escreveria testes para validar essa função usando arquivos pequenos de exemplo?
# Eu criaria arquivos pequenos contendo linhas válidas, linhas ignoradas (que não começam com “1”),
# valores inválidos, combinações de casos mistos e um arquivo vazio, permitindo comparar o resultado
# da função com o esperado em cada cenário

def calcular_totais(arquivo):
    total_registros = 0
    soma_centavos = 0
    erro = None

    with open(arquivo, "r", encoding="utf-8") as arq:
        for numero_linha, linha in enumerate(arq, start=1):
            linha = linha.strip()

            if not linha or linha[0] != "1":
                continue

            campo_valor = linha[-10:]

            if not campo_valor.isdigit():
                erro = f"Campo de valor possui caracteres inválidos - linha {numero_linha}"
                continue

            try:
                valor_centavos = int(campo_valor)
                soma_centavos += valor_centavos
                total_registros += 1
            except Exception:
                erro = f"Erro ao converter valor - linha {numero_linha}"
                continue

    if erro:
        total_registros = erro

    return {
        "total_registros": total_registros,
        "total_valores": soma_centavos / 100
    }
