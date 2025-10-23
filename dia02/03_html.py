# %%
import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
req = requests.get(url, headers=headers)

dfs = pd.read_html(req.text)
dfs
# %%
df_uf = dfs[1]
df_uf.to_csv("ufs.csv",sep=";",index=False)
# %%