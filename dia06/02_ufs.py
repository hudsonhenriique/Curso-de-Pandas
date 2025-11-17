#%%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

# Para evitar o erro 403 (Forbidden), simulamos um acesso via navegador
# definindo um User-Agent.
storage_options = {'User-Agent': 'Mozilla/5.0'}
dfs = pd.read_html(url, storage_options=storage_options)
uf = dfs[1]
uf

#%%
uf.dtypes

#%%
# Como tranformar um object em float
numero = "251 529,2"
# Formas erradas
float(numero)
uf["Área (km²)"].astype(float)
#%%
# Para converter é necessário transformar o dado
numero = numero.replace(" ", "").replace(",", ".")
numero
#%%
numero = float(numero.replace(" ", "").replace(",", "."))
numero
# %%
# Assim podemos definir uma função que faça isso em qualquer string da nosso DataFrame e utilizamos o Apply
def str_to_float(x:str):
    x = (x.replace(" ", "")
          .replace(",", ".")
          .replace("\xa0",""))
    return float(x)

# %%
# Aplica em cada elemento do nosso DataFrame
uf["Área (km²)"] =uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
# %%
uf.dtypes
# %%

def expt_to_anos(exp):
    exp = (exp.replace(",",".")
              .replace(" anos",""))
    return float(exp)

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(expt_to_anos)
uf.head()
# %%
def uf_to_regiao(uf):
     if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
          return "Centro-Oeste"
     elif uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
          return "Nordeste"
     elif uf in ["Rondônia", "Acre", "Amazonas", "Pará", "Amapá", "Roraima", "Tocantins"]:
          return "Norte"
     elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
          return "Sudeste"
     elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
          return "Sul"

uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf.head()

# %%

# Uma métrica para trabalharmos comparações
# Se PIB / Capita > 30.000
# +
# Mort Infantil < 15 / 1000
# +
# IDH (2010) > 700
# -> "Parece bom"

# Nao parece bom
#%%
def mortalidade_to_float(x:str):
    x = (x.replace("‰", "")
          .replace(",", ".")
              )
    return float(x)

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
uf.head()
#%%
# Navegando linha a linha e pegando a série da linha para ver se as comparações são verdadeiras
linha = uf.iloc[6]
(linha["PIB per capita (R$) (2015)"] > 30000 and
linha["Mortalidade infantil (/1000)"] < 15 and 
linha["IDH (2010)"] > 700)

#%%
def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and 
            linha["IDH (2010)"] > 700)
#%%
# Aplica em cada linha do DataFrame
# Axis 0, passa para a função cada uma das colunas
# Axis 1, passa para a função cada uma das linhas
uf.apply(classifica_bom, axis=1)
#%%
uf.apply(lambda x: x["PIB per capita (R$) (2015)"], axis=1)