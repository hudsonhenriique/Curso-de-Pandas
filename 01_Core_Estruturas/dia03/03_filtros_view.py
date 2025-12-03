#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep = ";")
clientes.head()
#
# %%
#Neste exemplo nós duplicamos dados, isso pode afetar a mémoria, usar com ponderações
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro].copy()

clientes_0["flag_1"] = 1
#
# %%
clientes_0.head()
# %%
A = [1,2]
B = A.copy()

print("A:",A)
print("B:",B)

B.append(3)

print("A:",A)
print("B:",B)
# %%