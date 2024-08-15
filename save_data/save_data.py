# Visualizando os clusters
sns.pairplot(rfm, hue='Cluster', palette='tab10')
plt.show()

# Tamanho de cada cluster
rfm['Cluster'].value_counts()
