# Análise de Vendas - Lumina Retail

Este projeto é um exercício de análise de dados utilizando Python e Pandas.  
O objetivo é explorar um conjunto de dados de vendas de uma loja fictícia chamada **Lumina Retail** e extrair informações úteis a partir desses dados.

## Objetivo do Projeto

Praticar conceitos fundamentais de análise de dados, incluindo:

- Leitura de arquivos CSV
- Manipulação de dados com Pandas
- Conversão de tipos de dados
- Criação de novas métricas
- Exploração inicial dos dados

## Estrutura do Projeto

analise-vendas-lumina-retail/

dados/  
  vendas_lumina.csv → conjunto de dados de vendas  

scripts/  
  analise_lumina.py → script principal de análise  

notebooks/  
  (pasta reservada para análises futuras em Jupyter Notebook)

README.md → documentação do projeto

## Tecnologias Utilizadas

- Python
- Pandas
- VS Code

## Etapas da Análise

1. Importação da biblioteca Pandas
2. Leitura do dataset de vendas
3. Conversão da coluna de data para formato datetime
4. Inspeção inicial dos dados
5. Criação da coluna de faturamento (preço × quantidade)

## Métrica Criada

**Faturamento**

Faturamento = Preço × Quantidade

Essa métrica permite entender quanto cada venda gerou de receita para a loja.

## Como Executar o Projeto

1. Clonar ou baixar o repositório
2. Abrir a pasta no VS Code
3. Executar o script no terminal:

python scripts/analise_lumina.py

## Próximos Passos do Projeto

- Calcular faturamento total
- Descobrir produtos mais vendidos
- Analisar faturamento por categoria
- Criar visualizações de dados
