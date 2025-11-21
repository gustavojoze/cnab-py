from datetime import datetime
from utils.validacoes import linha_valida, validar_cnpj, validar_data, validar_valor

from utils.formatacao import formatar_cnpj


# 2 Questão: 
# a) Como você testaria essa função para garantir que ela funciona em diferentes cenários?
# Coloquei testes e validações que permitiriam testar diferentes cenários, como:
# - Linhas com formatos corretos e incorretos, Datas inválidas 
# , Valores com caracteres não numéricos e Arquivo inexistente
# b) O que você faria se o CNPJ viesse com caracteres não numéricos? 
# Adicionei uma verificação para garantir que o CNPJ contenha apenas dígitos numéricos. 
# Se encontrar caracteres inválidos, função registra uma mensagem de erro específica para 
# essa linha, permitindo que o processamento continue para as outras linhas válidas.
def conversao_simples(caminho):
    linhasConvertidas = []

    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:

            for numero_linha, linha in enumerate(arquivo, start=1):

                if not linha_valida(linha) or len(linha) < 24 or len(linha) > 400:
                    continue

                if linha[0] == "1":

                    cnpj = linha[1:15]
                    data = linha[15:23]
                    valor = linha[23:33]

                    linhaConvertida = {}

                    erro_cnpj = validar_cnpj(cnpj, numero_linha)
                    if erro_cnpj:
                        linhaConvertida["cnpj"] = erro_cnpj
                    else:
                        linhaConvertida["cnpj"] = formatar_cnpj(cnpj)

                    linhaConvertida["data"] = validar_data(data, numero_linha)

                    linhaConvertida["valor"] = validar_valor(valor, numero_linha)

                    linhasConvertidas.append(linhaConvertida)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return linhasConvertidas
