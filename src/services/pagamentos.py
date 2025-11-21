from utils.validacoes import validacoes
# 3 Questão:
# a) Onde você centralizaria as regras de negócio para facilitar futuras mudanças?
# Coloquei as regras de negócio dentro de uma função interna chamada validacoes, assim, se for necessário alterar alguma regra,
# basta modificar essa função sem impactar o restante do código e facilita na padronização, mantém o codigo limpo e facil manutenção.
# b) Como garantir que mudanças nessas regras não quebrem funcionalidades antigas
# ao adicionar novos testes unitários que cubram os cenários existentes e os novos
# cenários introduzidos pelas mudanças nas regras de negócio.


def validar_pagamento(cnpj, valor):
    cnpj = str(cnpj)
    return {"status": validacoes(cnpj, valor)}
