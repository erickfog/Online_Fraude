# Projeto de Análise de Fraudes em Transações Bancárias

Este projeto tem como objetivo realizar uma análise abrangente de fraudes em transações bancárias utilizando técnicas de análise exploratória de dados (EDA) e modelagem estatística. O conjunto de dados utilizado contém informações sobre transações bancárias, incluindo detalhes sobre as transações e indicadores de fraude.

## Conjunto de Dados

O conjunto de dados utilizado neste projeto contém as seguintes colunas:

- `step`: Representa uma unidade de tempo no mundo real (1 passo equivale a 1 hora de tempo).
- `tipo`: Tipo de transação (CASH-IN, CASH-OUT, DEBIT, PAYMENT e TRANSFER).
- `quantidade`: Valor da transação na moeda local.
- `nomeOrig`: Cliente que iniciou a transação.
- `saldoAntigoOrig`: Saldo inicial antes da transação.
- `novoSaldoOrig`: Novo saldo após a transação.
- `nomeDest`: Cliente que é o destinatário da transação.
- `saldoAntigoDest`: Saldo inicial do destinatário antes da transação.
- `novoSaldoDest`: Novo saldo do destinatário após a transação.
- `ehFraude`: Indica se a transação é fraudulenta (0 para não fraudulenta, 1 para fraudulenta).

## Objetivos do Projeto

Os principais objetivos deste projeto incluem:

- Realizar uma análise exploratória dos dados para entender a distribuição das transações e identificar possíveis padrões de fraude.
- Visualizar as relações entre diferentes variáveis para identificar características associadas a transações fraudulentas.
- Aplicar técnicas estatísticas, como análise multivariada, para identificar fatores preditivos de fraudes em transações bancárias.
- Explorar técnicas de modelagem preditiva para prever transações fraudulentas com base em características específicas das transações.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

1. **Análise Exploratória de Dados (EDA)**: Explorar os dados, visualizar distribuições, identificar padrões e relações entre variáveis.
2. **Análise Multivariada**: Aplicar técnicas estatísticas para entender as relações complexas entre múltiplas variáveis.
3. **Modelagem Preditiva**: Explorar técnicas de modelagem preditiva para prever transações fraudulentas.
4. **Conclusões e Recomendações**: Resumir os principais resultados da análise e fornecer recomendações para prevenção de fraudes em transações bancárias.

## Como Usar

Para utilizar este projeto, siga estas etapas:

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter todas as dependências instaladas (Python, Jupyter Notebook, bibliotecas Python listadas no arquivo `requirements.txt`).
3. Execute o notebook Jupyter `OnlineFraudDetection.ipynb` para reproduzir a análise.
4. Explore os resultados e adapte o código conforme necessário para atender aos seus objetivos específicos.
5. O desafio de engenharia de tados está na pasta `test_data_eng` e execute o arquivo `eng_data.py` ou utilize o `eng_data_mobi2buy.ipynb`(este arquivo contém as saídas especificadas). 

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).


