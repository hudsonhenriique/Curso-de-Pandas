# 🐼 Pandas Analytics: Data Wrangling & ETL

## 📌 Visão Técnica
Este repositório reúne pipelines de tratamento e análise de dados utilizando a biblioteca **Pandas**, demonstrando a capacidade de transformar dados brutos e desestruturados em datasets analíticos prontos para tomada de decisão.

Diferente de scripts básicos de manipulação, este portfólio aplica técnicas avançadas de **reshaping** (remodelagem geométrica de dados) e automação de leitura de arquivos, essenciais para lidar com cenários reais de engenharia de dados.

## ⚙️ Competências Demonstradas

### 1. Data Cleaning & Sanitização
* Tratamento de valores nulos (`fillna`, `dropna`) e remoção de duplicatas para garantir integridade.
* Padronização de tipos de dados (Casting) e normalização de textos.

### 2. Engenharia de Atributos (Feature Engineering)
* Uso de `apply` e funções lambda para criação de regras de negócio complexas linha a linha.
* Manipulação temporal (`datetime`) para cálculos de projeção de datas e vencimentos.

### 3. Advanced Reshaping & Consolidação
* Transformação de dados entre formatos "Largo" (Wide) e "Longo" (Long) utilizando **`stack`** e **`unstack`**.
* Criação de tabelas dinâmicas executivas com **`pivot_table`**.
* Consolidação de múltiplos arquivos CSV em um único Dataframe via loops de leitura (`os.listdir`) e `concat`.

## 📂 Estrutura do Projeto

O repositório está organizado conforme o ciclo de vida do tratamento de dados:

### `01_Core_Estruturas`
Fundamentos de manipulação de objetos `Series` e `DataFrames`, incluindo indexação e fatiamento (slicing) de dados.

### `02_Sanitizacao_Dados`
Scripts focados na limpeza do dataset: identificação de anomalias, tratamento de dados faltantes (NA) e correção de tipagem.

### `03_Engenharia_Atributos`
Criação de novas variáveis analíticas a partir dos dados existentes, aplicando lógica condicional e operações vetoriais.

### `04_Agregacao_Modelagem`
Técnicas de sumarização de dados (`groupby`), métricas estatísticas e união de tabelas relacionais (`merge`/`join`).

### `05_Laboratorio_Cases` (Aplicações Reais)
Projetos práticos que resolvem problemas de negócio específicos:
* **Case Cartão de Crédito:** Algoritmo para projetar fluxo de caixa futuro "explodindo" parcelas de vendas (`explode` + `DateOffset`).
* **Case Homicídios (IPEA):** ETL que lê múltiplos arquivos CSV de uma pasta, consolida os dados e remodela a tabela para análise temporal.

## 💡 Highlight: Projeção Financeira (Snippet)

Um dos desafios resolvidos envolve a projeção de parcelas futuras de vendas no cartão de crédito, transformando uma linha de venda em múltiplas linhas de recebimento (Fluxo de Caixa).

```python
# Exemplo de lógica utilizada no Case Cartão de Crédito
def calcDtParcela(row):
    # Projeta a data de vencimento baseada no número da parcela
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    return f"{dt.year}-{dt.month}"

# 1. Cria uma lista com o range de parcelas
df["ordemParcela"] = df.apply(lambda row: [i for i in range(row['qtParcelas'])], axis=1)

# 2. Explode a lista, criando uma linha para cada parcela
df_explode = df.explode("ordemParcela")

# 3. Calcula a data real de cada parcela
df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)
```
## 🚀 Como Executar
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install pandas openpyxl
   ```
3. Navegue até a pasta 05_Laboratorio_Cases para ver os scripts de ETL em ação.
   
## 🔗 Conecte-se Comigo

Acompanhe meu progresso e vamos trocar ideias!

* **LinkedIn:** [Hudson Henrique](https://www.linkedin.com/in/hudsonhenri)
* **GitHub:** [Hudson Henrique](https://github.com/hudsonhenriique)
