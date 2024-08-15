O objetivo principal deste projeto é aplicar técnicas de clustering para identificar segmentos de clientes com comportamentos de compra similares. Com isso, é possível direcionar estratégias de marketing e personalizar ofertas de acordo com os perfis identificados.

## Dataset

O dataset utilizado neste projeto foi extraído do [Kaggle Datasets](https://www.kaggle.com/), que contém dados de transações de compras realizadas por clientes.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para análise de dados e machine learning.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **NumPy**: Biblioteca para operações numéricas.
- **Matplotlib e Seaborn**: Bibliotecas para visualização de dados.
- **Scikit-learn**: Biblioteca para machine learning, utilizada para aplicação do algoritmo K-means.

## Metodologia

1. **Carregamento e Exploração dos Dados**: Os dados foram carregados e explorados para entender a estrutura e identificar possíveis valores ausentes ou anomalias.
2. **Pré-processamento**: Realizou-se a limpeza dos dados, normalização e seleção de variáveis relevantes.
3. **Clustering com K-means**: O algoritmo K-means foi aplicado para segmentação dos clientes, gerando 5 clusters distintos.
4. **Análise dos Clusters**: Os clusters foram analisados para interpretar as características de cada grupo de clientes.

## Resultados

Os resultados da segmentação mostraram grupos distintos de clientes, cada um com padrões de comportamento de compra específicos. Estes insights podem ser utilizados para melhorar a personalização de campanhas de marketing e otimizar a experiência dos clientes.

## Próximos Passos

Futuras iterações deste projeto podem incluir a exploração de outros algoritmos de clustering, como DBSCAN ou Hierarchical Clustering, e a integração de novas variáveis ao modelo.

## Como Executar

1. Clone o repositório.
2. Instale as dependências listadas no `requirements.txt`.
3. Execute o script `segmentacao_clientes.py`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
