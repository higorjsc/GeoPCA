import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np


# file_path = 'assay_pca.csv'
file = "assay_pca.csv"
naValues = "-99.00"
assay = pd.read_csv(file, na_values=naValues)

# Especifique os códigos CLI que você deseja incluir na análise
coluna = "CLI"

litologias = [
            'HF', 
            'HG', 
            'HGO', 
            'IC', 
            'IGO', 
            'IF', 
            'IFR'
        ]
# Selecionar as colunas para PCA
varNumericas = [
                "feglc", 
                "alglc", 
                "siglc", 
                "mnglc", 
                "mgglc", 
                "caglc", 
                "pfglc", 
                "pglc", 
                ]

assay = assay[assay[coluna].isin(litologias)]
pcaDataframe = assay[varNumericas].dropna()

# Padronização dos dados
scaler = StandardScaler()
pcaDataframeNormalizado = scaler.fit_transform(pcaDataframe)

# Preparar os dados de cores CLI após a filtragem
colunaFiltrada = assay[coluna][pcaDataframe.index]

# Crie um mapeamento de códigos CLI para cores
colunaItens = colunaFiltrada.unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(colunaItens)))
color_map = dict(zip(colunaItens, colors))

# PCA para 2 componentes para o gráfico 2D
pca2d = PCA(n_components=2)
pca2dComponents = pca2d.fit_transform(pcaDataframeNormalizado)

# Gráfico 2D
plt.figure(figsize=(8, 6))
for cli, color in color_map.items():
    plt.scatter(pca2dComponents[colunaFiltrada == cli, 0],
                pca2dComponents[colunaFiltrada == cli, 1],
                label=cli, color=color)
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('PCA 2D')
plt.legend()
plt.show()

# PCA para 3 componentes para o gráfico 3D
pca_3d = PCA(n_components=3)
principal_components_3d = pca_3d.fit_transform(pcaDataframeNormalizado)

# Gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
for cli, color in color_map.items():
    mask = (colunaFiltrada == cli)
    ax.scatter(principal_components_3d[mask, 0],
               principal_components_3d[mask, 1],
               principal_components_3d[mask, 2],
               label=cli, color=color)
ax.set_xlabel('Componente Principal 1')
ax.set_ylabel('Componente Principal 2')
ax.set_zlabel('Componente Principal 3')
ax.set_title('PCA 3D')
ax.legend()
plt.show()