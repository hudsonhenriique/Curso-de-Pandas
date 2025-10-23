# ARQUIVO MUITO COMENTADO PARA ESTUDAR MAIS ESSA PARTE, REVER ESSA AULA OUTRAS VEZES
#%%
import pandas as pd

# Lê um arquivo CSV para um DataFrame do pandas.
# O caminho "../data/transacoes.csv" indica que o arquivo está na pasta 'data', um nível acima do diretório atual.
# O parâmetro sep=";" informa ao pandas que as colunas no arquivo são separadas por ponto e vírgula, não por vírgula.
df = pd.read_csv("../data/transacoes.csv",sep=";")
df
#%%
# O atributo .shape retorna uma tupla com o número de linhas e colunas do DataFrame (linhas, colunas).
df.shape
#%%
# O método .info() exibe um resumo conciso do DataFrame.
# Inclui o tipo de índice, as colunas, a contagem de valores não nulos e o uso de memória.
# memory_usage="deep" faz uma introspecção mais profunda para calcular o uso real de memória, especialmente útil para colunas com strings.
df.info(memory_usage="deep")
#%%
# O atributo .dtypes retorna uma Série com o tipo de dado de cada coluna.
df.dtypes
#%%
# Cria um dicionário para renomear colunas. A chave é o nome antigo e o valor é o nome novo.
rename_columns = {"QtdePontos":"QtPontos",
                  "DescSistemaOrigem": "SistemaOrigem" 
                  }

# O método .rename() é usado para alterar os nomes das colunas.
# inplace=True modifica o DataFrame 'df' diretamente, sem a necessidade de atribuí-lo a uma nova variável (como em 'df = df.rename(...)').
df.rename(columns=rename_columns,inplace=True)
#%%
# Seleciona uma única coluna ('IdCliente').
# O resultado é um objeto do tipo pd.Series.
df["IdCliente"]
#%%
# Seleciona uma única coluna, mas usando colchetes duplos [[]].
# O resultado é um DataFrame com uma única coluna, em vez de uma Series.
df[["IdCliente"]]
#%%
# Seleciona múltiplas colunas passando uma lista de nomes de colunas.
# O resultado é um novo DataFrame contendo apenas as colunas especificadas.
df[["IdCliente","QtPontos","SistemaOrigem"]]
# %%
# Exibir o DataFrame completo. Semelhante a um `SELECT *` em SQL.
df

# %%
# Semelhante a `SELECT IdCliente FROM df` em SQL.
# Nota: Os nomes das colunas são sensíveis a maiúsculas e minúsculas. O correto é "IdCliente".
df[["IdCliente"]]

# %%
# Semelhante a `SELECT IdCliente, QtPontos FROM df LIMIT 5` (pegando os últimos 5).
# O método .tail(5) retorna as últimas 5 linhas do DataFrame.
# Nota: Corrigido "idCliente" para "IdCliente" e "qtPontos" para "QtPontos".
df[["IdCliente", "QtPontos"]].tail(5)

# %%
# Semelhante a `SELECT IdCliente, idTransacao, QtPontos FROM df LIMIT 5`.
# O método .head(5) retorna as 5 primeiras linhas do DataFrame.
# Nota: Corrigido "idCliente" para "IdCliente" e "qtPontos" para "QtPontos".
df[["IdCliente", "idTransacao", "QtPontos"]].head(5)
# %%
# Cria uma lista com todos os nomes de colunas do DataFrame.
colunas = list(df.columns)
# Ordena a lista de nomes de colunas em ordem alfabética.
colunas.sort()
colunas

# Reordena as colunas do DataFrame 'df' de acordo com a lista 'colunas' que foi ordenada alfabeticamente.
df = df[colunas]
df