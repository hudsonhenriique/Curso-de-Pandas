#%%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv",sep=";")
df.head()

# %%
# Cria uma nova coluna 'pontos_100' somando 100 a cada valor da coluna 'qtdePontos'.
# Esta é uma operação vetorizada, muito mais rápida que um loop.
df["pontos_100"] = df["qtdePontos"] + 100
df.head()

# %%
# Demonstração de como fazer a mesma operação da célula anterior usando um loop for.
# Este método é menos eficiente e não é o recomendado em pandas.
nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append( i+100)

nova_coluna

# %%
# Cria a coluna 'emailTwitch' somando os valores das flags (que são 0 ou 1).
# O resultado indica se o cliente está em uma (1), ambas (2) ou nenhuma (0) das plataformas.
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%
# Multiplica as flags. O resultado será 1 apenas se AMBAS as colunas ('flEmail' e 'flTwitch') forem 1.
# Funciona como um operador lógico "E" (AND).
df["flEmail"] * df["flTwitch"]

# %%
# Cria 'qtdeSocial' somando todas as flags de redes sociais.
# O resultado é o número total de plataformas em que cada cliente está presente.
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df

# %%
# Cria 'todas_social' multiplicando todas as flags.
# O resultado será 1 apenas se o cliente estiver em TODAS as redes sociais, e 0 caso contrário.
df["todas_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df

# %%
# Apenas exibe a coluna 'qtdePontos' original para referência.
df["qtdePontos"]

# %%
# Aplica a transformação logarítmica na coluna de pontos usando a função log do numpy.
# Adiciona 1 para evitar erro de log(0), que é indefinido.
df["logPontos"] = np.log(df["qtdePontos"]+1)
# O método .describe() mostra estatísticas básicas da nova coluna, como média, desvio padrão, etc.
df["logPontos"].describe()

# %%
# Usa a biblioteca matplotlib para criar e exibir um histograma.
# Um histograma é um gráfico que mostra a distribuição de frequência dos dados.
import matplotlib.pyplot as plt

plt.grid(True)
plt.hist(df["logPontos"])
plt.show()