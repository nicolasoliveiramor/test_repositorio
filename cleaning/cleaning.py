# Removendo entradas nulas
df.dropna(inplace=True)

# Filtrando apenas transações positivas
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Criando uma coluna de receita
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Resumo dos dados
df.describe()
