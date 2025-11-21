
from utils.validacoes import linha_valida

 # 1 Questão:
    # a) Como você trataria um arquivo com linhas vazias ou linhas com tamanho incorreto?
    # a – Criaria uma função para validar estas informações, facilitando a verificação de linhas válidas, evitando processar linhas
    # vazias ou incorretas, deixando o código mais organizado, limpo e fácil de manter.
    # b) Onde você colocaria a lógica de validação (mesma função, função separada, classe, etc.)?
    #  Justifique.
    # b – Colocaria essa lógica de validação em uma função separada e acessivel, pois fica mais fácil de identificar, é mais semântico, centralizado,
    # melhora a legibilidade, evita repetição e mantém a função principal focada apenas na leitura e contagem, deixando mais limpo o codigo.
    
def contarTiposLinhas(arquivoCNAB):
    contagensTipo = {"header":0,"detalhes":0,"trailer":0}
    try:
        with open(arquivoCNAB,"r",encoding="utf-8") as arquivo:
            for linha in arquivo:   
                linha = linha.strip()
                if not linha_valida(linha):
                    continue
                tipo = linha[0]
                if tipo == "0": contagensTipo["header"] += 1
                elif tipo == "1": contagensTipo["detalhes"] += 1
                elif tipo == "9": contagensTipo["trailer"] += 1
        return contagensTipo
    except FileNotFoundError:
        return {"erro":"Arquivo não encontrado."}
    except Exception as e:
        return {"erro":f"Erro inesperado: {str(e)}"}
