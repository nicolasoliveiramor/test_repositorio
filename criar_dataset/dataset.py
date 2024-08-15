# O dataset pode ser baixado do Kaggle e carregado localmente.
df = pd.read_csv('Online_Retail.csv')

# Como exemplo, vamos usar um dataset de amostra:
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
df = pd.read_excel(url)

# Visualizar as primeiras linhas
df.head()
