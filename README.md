# Projeto CNAB Modular 

Este projeto implementa o processamento de arquivos CNAB de forma organizada e modular, seguindo boas práticas de arquitetura e garantindo confiabilidade através de testes automatizados

## Estrutura e explicações:

```bash
project/
  src/
    data/                  # arquivos do projeto (entrada e saída)
        arquivosExemplos/  # CNABs usados nos testes e execuções
        comprovantes/      # comprovantes gerados pela aplicação

    utils/                 # funções auxiliares reutilizáveis
      validacoes.py        # validação de linhas, CNPJ, datas e valores
      formatacao.py        # formatação de CNPJ e valores

    services/                # regras de negócio do sistema
      pagamentos.py        # definição do status do pagamento
      conversao.py         # ConversaoSimples (conversão de registros)
      totais.py            # cálculo dos totais

    infrastructure/        # comunicação com o mundo externo (arquivos)
      leitura.py           # contarTiposLinhas
      comprovantes.py      # gerar_comprovante

  tests/                   # testes automatizados com pytest
    ...                    # validações de cada módulo

  README.md
  requirements.txt

```

## Requisitos

- Python
- Pip
- Virtualenv (opcional, mas recomendado)


## Como Rodar no seu computador, apos git clone?
```bash
# Entrar no projeto
cd meu-projeto

# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Executar testes
pytest -vv
```


## Como usar por dentro?

Agora apenas execute o codigo, e veja os resultados no terminal.
As questões estão respondida em cada função criada, use o comando "CTRL+botão do mouse" em cima delas para ser levados aos exercicios respondidos.

```python
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

```
1 Questão:  
a) Como você trataria um arquivo com linhas vazias ou linhas com tamanho incorreto?  
Criaria uma função para validar estas informações, facilitando a verificação de linhas válidas, evitando processar linhas vazias ou incorretas, deixando o código mais organizado, limpo e fácil de manter.  

b) Onde você colocaria a lógica de validação (mesma função, função separada, classe, etc.)? Justifique.  
Colocaria essa lógica de validação em uma função separada e acessível, pois fica mais fácil de identificar, é mais semântico, centralizado, melhora a legibilidade, evita repetição e mantém a função principal focada apenas na leitura e contagem, deixando o código mais limpo.  


2 Questão:  
a) Como você testaria essa função para garantir que ela funciona em diferentes cenários?  
Coloquei testes e validações que permitiriam testar diferentes cenários, como:  
- Linhas com formatos corretos e incorretos  
- Datas inválidas  
- Valores com caracteres não numéricos  
- Arquivo inexistente  

b) O que você faria se o CNPJ viesse com caracteres não numéricos?  
Adicionei uma verificação para garantir que o CNPJ contenha apenas dígitos numéricos.  
Se encontrar caracteres inválidos, a função registra uma mensagem de erro específica para essa linha, permitindo que o processamento continue para as outras linhas válidas.  


3 Questão:  
a) Onde você centralizaria as regras de negócio para facilitar futuras mudanças?  
Coloquei as regras de negócio dentro de uma função interna chamada `validacoes`. Assim, se for necessário alterar alguma regra, basta modificar essa função sem impactar o restante do código, facilitando padronização, organização e manutenção.  

b) Como garantir que mudanças nessas regras não quebrem funcionalidades antigas?  
Ao adicionar novos testes unitários que cubram os cenários existentes e os novos cenários introduzidos pelas mudanças nas regras de negócio.  


4 Questão:  
a) Como você organizaria a pasta de saída desses comprovantes?  
Colocaria o nome dos comprovantes com o **ID do comprovante**, para facilitar a identificação,  
e organizaria os arquivos em subpastas por ano e mês de processamento,  
permitindo localizar tudo com facilidade.  
Também colocaria o **CNPJ formatado no nome do arquivo** para melhorar a visualização.  

b) O que você faria se o sistema não tivesse permissão de escrita na pasta configurada?  
Usaria a pasta temporária do sistema operacional como alternativa,  
garantindo que o comprovante ainda possa ser gerado e salvo em outro local,  
e exibiria uma mensagem de aviso sobre a mudança de local.  


5 Questão:  
a) Como você lidaria com uma linha de detalhe com valor inválido (por exemplo, letras no campo numérico)?  
Coloquei uma verificação para identificar valores inválidos e registrar um erro específico para essas linhas, permitindo que o processamento continue para as outras linhas válidas.  

b) Como você escreveria testes para validar essa função usando arquivos pequenos de exemplo?  
Eu criaria arquivos pequenos contendo linhas válidas, linhas ignoradas (que não começam com “1”), valores inválidos, combinações de casos mistos e um arquivo vazio, permitindo comparar o resultado da função com o esperado em cada cenário.  

6.1 O que é Docker?  
Docker é uma plataforma que permite empacotar, executar e isolar aplicações  
em ambientes chamados containers, garantindo que o programa funcione igual  
em qualquer máquina, independentemente de configurações locais, versões ou  
dependências instaladas.  

6.2 O que é uma imagem Docker?  
Uma imagem é um modelo congelado contendo código, bibliotecas, dependências  
e configurações, funcionando como um snapshot do sistema, permitindo criar  
containers idênticos sempre que necessário, sem variações entre máquinas.  

6.3 O que é um container?  
Um container é a execução ativa de uma imagem, rodando como uma instância  
isolada, leve e independente, permitindo que a aplicação use apenas o que  
precisa, sem interferir no restante do sistema ou depender do ambiente local.  

6.4 Para que serve um Dockerfile?  
O Dockerfile descreve como construir a imagem, definindo qual linguagem usar,  
quais bibliotecas instalar, quais arquivos copiar, e qual comando executar ao  
iniciar o container, funcionando como o manual de construção do ambiente.  

6.5 Como executar um script CNAB dentro de um container?  
Para rodar um script CNAB em um container, cria-se um Dockerfile contendo o  
Python e o script, constrói-se a imagem com `docker build`, e executa-se o  
container com um volume montado, permitindo que os arquivos CNAB fiquem fora  
do container, enquanto a lógica roda dentro dele.  

7.1 Cite 3 boas práticas de desenvolvimento backend  
Manter código limpo e legível, criar funções pequenas com responsabilidade  
única, separar regras de negócio da lógica técnica e utilizar testes  
automatizados.  

7.2 Como nomearia variáveis e funções em projetos CNAB?  
Nomes claros como `linha_bruta`, `tipo_registro`, `valor_centavos`,  
`cnpj_formatado`, `header`, `trailer`, `detalhe`, além de funções como  
`ler_arquivo_cnab`, `processar_linha`, `extrair_campos`, `validar_campos`,  
`identificar_tipo_registro`, `formatar_cnpj`, `formatar_data`,  
`formatar_valor`, `gerar_linha_cnab`, `montar_header`, `montar_detalhe`,  
`montar_trailer`, `calcular_totais` e `escrever_arquivo`.  

7.3 O que é um teste automatizado e por que é importante?  
Um teste automatizado é um código que executa funções e valida resultados  
automaticamente, garantindo que alterações futuras não quebrem funções já  
existentes, mantendo confiança, segurança e estabilidade no backend.  

 7.4 Como organizaria a estrutura de pastas de um pequeno projeto CNAB?  
 Uma estrutura organizada pode seguir o padrão:



    
    project/
    src/
      data/                  # arquivos do projeto (entrada e saída)
          arquivosExemplos/  # CNABs usados nos testes e execuções
          comprovantes/      # comprovantes gerados pela aplicação
      utils/                 # funções auxiliares reutilizáveis
        validacoes.py        # validação de linhas, CNPJ, datas e valores
        formatacao.py        # formatação de CNPJ e valores
      controller/            # para usar rotas
      repository/            # para usar banco de dados no projeto
      services/                # regras de negócio do sistema
        pagamentos.py        # definição do status do pagamento
        conversao.py         # ConversaoSimples (conversão de registros)
        totais.py            # cálculo dos totais
  
      infrastructure/        # comunicação com o mundo externo (arquivos)
        leitura.py           # contarTiposLinhas
        comprovantes.py      # gerar_comprovante
  
      tests/                   # testes automatizados com pytest
      ...                    # validações de cada módulo

    README.md
    requirements.txt
