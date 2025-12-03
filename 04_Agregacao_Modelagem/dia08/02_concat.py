#%%
import pandas as pd
#%%
df=pd.DataFrame({
    "Cliente": [1,2,3,4,5],
    "Nome": ['Hudson',"Henrique",'Marilaine','Thais','Kevin'],
})
df
#%%
df_02 = pd.DataFrame({
    "Cliente":[6,7,8],
    "Nome":["Wallace","Lorena",'Rosane'],
    "Idade":[32,29,31]
})
df_02

# %%
df_03 = pd.DataFrame({
    "Idade": [32,34,19,54,33]})
df_03
# %%
dfs = [df,df_02]
pd.concat(dfs,ignore_index=True)
#%%
pd.concat([df,df_03],axis=1)

# %%
df_03 = df_03.sort_values(by='Idade').reset_index(drop=True)
df_03
# %%
pd.concat([df,df_03],axis=1)
# %%
