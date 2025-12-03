# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

# Encontra o valor máximo de pontos na coluna 'qtdePontos'.
max_ponto = clientes["qtdePontos"].max()
# Cria um filtro para encontrar as linhas onde 'qtdePontos' é igual ao máximo.
filtro = clientes["qtdePontos"] == max_ponto
# Exibe os clientes com a pontuação máxima.
clientes[filtro]

# %%

# Ordena os clientes por 'qtdePontos' (do maior para o menor),
# pega os 5 primeiros (.head(5)) e seleciona apenas a coluna 'idCliente'.
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
                 .head(5)["idCliente"] )

# O resultado 'top_5' é uma Series do pandas.
type(top_5)

# %%
# Exibe o DataFrame original de clientes.
clientes

# %%

# Cria um DataFrame de exemplo para demonstrar a ordenação.
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533],
    }
)

# Exibe o DataFrame de exemplo.
brinquedo

# %%

# Ordena o DataFrame por múltiplos critérios:
# 1. 'salario' em ordem decrescente (do maior para o menor).
# 2. Em caso de salários iguais, ordena por 'idade' em ordem crescente (do menor para o maior).
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])