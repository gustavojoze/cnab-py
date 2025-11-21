import os
from infrastructure.leitura import contarTiposLinhas
from services.conversao import conversao_simples
from services.totais import calcular_totais
from infrastructure.comprovantes import gerar_comprovante
from services.pagamentos import validar_pagamento

BASE_DIR = os.path.dirname(__file__)
ARQ = os.path.join(BASE_DIR, "data/arquivosExemplos/cnab_exemplo1.txt")

#Questão 1
print("Questão 1:")
print(contarTiposLinhas(ARQ))
#Questão 2
print("Questão 2:")
print(conversao_simples(ARQ))
#Questão 3
print("Questão 3:")
print(validar_pagamento("123456780001909", 150.0))
#Questão 4
print("Questão 4:")
print(gerar_comprovante("123456780001939", 150.0))
#Questão 5
print("Questão 5:")
print(calcular_totais(ARQ))
