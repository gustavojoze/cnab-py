
import os, uuid, tempfile
from datetime import datetime
from services.pagamentos import validar_pagamento
from utils.formatacao import formatar_cnpj, formatar_valor_brasil

# 4 Questões:
# a) Como você organizaria a pasta de saída desses comprovantes?
# Colocaria o nome dos comprovantes com o id do comprovante, para facilitar a identificação,
# e organizaria os arquivos em subpastas por ano e mês de processamento,
# para organizar e conseguir encontrar o arquivo com mais facilidade,e colocaria o cnpj 
# formatado no próprio no nome do arquivo para melhor visualização.
# b) O que você faria se o sistema não tivesse permissão de escrita na pasta configurada
# Usaria a pasta temporária do sistema operacional como alternativa,
# garantindo que o comprovante ainda possa ser gerado e salvo em outro local. E colocaria
# uma mensagem de aviso para o usuário sobre a mudança de local.

def gerar_comprovante(cnpj, valor):
    ano_atual = datetime.now().strftime("%Y")
    mes_atual = datetime.now().strftime("%m")

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    pasta_base = os.path.join(BASE_DIR, "data", "comprovantes")
    pasta_destino = os.path.join(pasta_base, ano_atual, mes_atual)

    try:
        os.makedirs(pasta_destino, exist_ok=True)
        pasta_final = pasta_destino
    except PermissionError:
        pasta_final = tempfile.gettempdir()
        print(f" Aviso: Sem permissão para salvar em '{pasta_destino}'. Salvando em '{pasta_final}'.")

    id = str(uuid.uuid4())
    cnpj_formatado = formatar_cnpj(cnpj)
    valor_formatado = formatar_valor_brasil(valor)
    data_atual = datetime.now().strftime("%d/%m/%Y")
    status = validar_pagamento(cnpj, valor)["status"]

    nome_arquivo = os.path.join(pasta_final, f"comprovante_{id}.txt")

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arq:
            arq.write("COMPROVANTE DE PROCESSAMENTO\n")
            arq.write(f"ID: {id}\n")
            arq.write(f"CNPJ: {cnpj_formatado}\n")
            arq.write(f"VALOR: R$ {valor_formatado}\n")
            arq.write(f"DATA PROCESSAMENTO: {data_atual}\n")
            arq.write(f"STATUS: {status}")

        return {"mensagem": "Comprovante gerado com sucesso!", "arquivo": nome_arquivo, "status": status}

    except PermissionError:
        return {"erro": "O sistema não tem permissão para escrever o comprovante.", "arquivo_tentado": nome_arquivo}