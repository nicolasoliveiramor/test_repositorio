# Criando a Tabela RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (df['InvoiceDate'].max() - x.max()).days,
    'InvoiceNo': 'count',
    'Revenue': 'sum'
}).reset_index()

# Renomeando colunas
rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Visualizando as primeiras linhas da Tabela RFM
rfm.head()
