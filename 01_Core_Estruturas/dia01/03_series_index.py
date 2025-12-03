# %%
import pandas as pd

idades = [32,38,30,30,31,35,25,29,31,37,27,23,36,33,36]

series_idades = pd.Series(idades)
series_idades
# %%
print(idades[-1])
print(series_idades[14])
# %%
print(idades[0])
print(series_idades[0])
#%%
series_idades = series_idades.sort_values()
series_idades
#%%
print(series_idades.iloc[0])
print(series_idades.iloc[-1])
print(series_idades.iloc[:3])
print(series_idades.iloc[::-1])
#
