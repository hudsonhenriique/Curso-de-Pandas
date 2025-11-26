# %%
# 06.04 - Quem teve mais transações de Streak?

import pandas as pd

# %%
transacoes = pd.read_csv("../../data/transacoes.csv", sep=';')
transacoes.head()

# %%
transacao_produto = pd.read_csv("../../data/transacao_produto.csv", sep=';')
transacao_produto.head()

# %%
produtos = pd.read_csv("../../data/produtos.csv", sep=';')
produtos.head()

#%%
# Garante que a coluna de merge 'IdProduto' tenha o mesmo tipo em ambos os DataFrames
produtos['IdProduto'] = produtos['IdProduto'].astype(int)
transacao_produto['IdProduto'] = pd.to_numeric(transacao_produto['IdProduto'], errors='coerce')
transacao_produto = transacao_produto.dropna(subset=['IdProduto'])
transacao_produto['IdProduto'] = transacao_produto['IdProduto'].astype(int)
#%%

produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"]

(transacoes.merge(transacao_produto, on="IdTransacao", how="left")
           .merge(produtos,on=["IdProduto"],how='inner')
           .groupby(by='IdCliente')['IdTransacao']
           .count()
           .sort_values(ascending=False)
           .head(1)
)
#%%

 #%%
# Outra maneira de fazer!!

# transacao_produto['IdProduto'] = pd.to_numeric(transacao_produto['IdProduto'], errors='coerce')
# transacao_produto = transacao_produto.dropna(subset=['IdProduto'])
# transacao_produto['IdProduto'] = transacao_produto['IdProduto'].astype(int)
# produto_alvo = produtos[produtos["DescNomeProduto"] == "Presença Streak"].copy()

# #%%
# if len(produto_alvo) == 0:
#     print("Erro: Produto 'Presença Streak' não encontrado na base de produtos.")
# else:

#     ranking = (
#         produto_alvo                                      
#         .merge(transacao_produto, on="IdProduto", how="inner") 
#         .merge(transacoes, on="IdTransacao", how="inner")      
#         .groupby(by="IdCliente")["IdTransacao"]
#         .count()
#         .sort_values(ascending=False)
#         .head(1)
#     )
# #%%
#     print("Cliente Campeão de Streak:")
#     print(ranking)

