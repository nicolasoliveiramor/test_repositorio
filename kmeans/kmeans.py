# Definindo o modelo K-means
kmeans = KMeans(n_clusters=4, random_state=42)

# Ajustando o modelo
kmeans.fit(rfm_scaled)

# Atribuindo rótulos aos clusters
rfm['Cluster'] = kmeans.labels_

# Visualizando as primeiras linhas com os clusters
rfm.head()
