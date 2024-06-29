import subprocess
import sys

# Função para instalar uma biblioteca usando pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Lista de pacotes necessários
required_packages = ["pandas", "sklearn", "matplotlib", "numpy"]

# Verifica e instala pacotes
print("Verificando dependencias...")
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} não está instalado. Instalando...")
        if not package == "sklearn":
            install_package(package)
        else:
            install_package('scikit-learn')

print("Tudo certo!")

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# BOAS VINDAS
print("\nOlá!\n")
print("Coloque o arquivo assay na mesma pasta que este script!\n")

while True:
    file = input("Informe o nome e extensão do arquivo (Ex: arquivo.csv): ")
    naValues = input("Informe o código para valores não atribuídos (Ex: -99.00): ")
    try:
        assay = pd.read_csv(file, na_values=naValues)
        print("Arquivo lido com sucesso!\n")
        break
    except FileNotFoundError:
        print("Erri: Arquivo não encontrado ou código inválido!\n")
        
# COLUNA DE LITOLOGIA  
while True:
    coluna = input("Informe o nome da coluna de litologias no assay: ")
    try:
        if coluna not in assay.columns:
            raise ValueError(f"A coluna '{coluna}' não está presente no DataFrame.\n")
        break
    except ValueError as ve:
        print(f"Erro: {ve}")
        
# LITOLOGIAS
while True:
    litosInput = input("Informe o nome de todas as litologias para análise (ex: xisto, gnaisse, coal): ")
    litoCodes = [litologia.strip() for litologia in litosInput.split(',')]
    try:
        assayFiltrado = assay[assay[coluna].isin(litoCodes)]
        if assayFiltrado.empty:
            raise ValueError("Nenhuma das litologias fornecidas está presente no arquivo.\n")
        break
    except ValueError as ve:
        print(f"Erro: {ve}")

# VARIÁVEIS NÚMERICAS
while True:
    variaveisNumericasInput = input("Informe as variáveis para análise (ex: FEPPM, Fe%, Al, Mn): ")
    variaveisNumericas = [coluna.strip() for coluna in variaveisNumericasInput.split(',')]
    try:
        # Verifica se todas as colunas fornecidas pelo usuário existem no DataFrame
        colunasFaltantes = [coluna for coluna in variaveisNumericas if coluna not in assayFiltrado.columns]
        if colunasFaltantes:
            raise ValueError(f"As seguintes colunas não estão no assay: {', '.join(colunasFaltantes)}\n")
        pcaDataframe = assayFiltrado[variaveisNumericas].dropna()
        break
    except ValueError as ve:
        print(f"Erro: {ve}")

# Padronização dos dados
scaler = StandardScaler()
pcaDataframeNormalizado = scaler.fit_transform(pcaDataframe)

# PCA para 2 componentes para o gráfico 2D
pca2d = PCA(n_components=2)
pca2dComponents = pca2d.fit_transform(pcaDataframeNormalizado)

# Preparar os dados de cores CLI após a filtragem
colunaFiltrada = assay[coluna][pcaDataframe.index]

# Crie um mapeamento de códigos CLI para cores
colunaItens = colunaFiltrada.unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(colunaItens)))
color_map = dict(zip(colunaItens, colors))

# Gráfico 2D
plt.figure(figsize=(8, 6))
for coluna, color in color_map.items():
    plt.scatter(
        pca2dComponents[colunaFiltrada == coluna, 0],
        pca2dComponents[colunaFiltrada == coluna, 1],
        label=coluna, color=color
    )
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('PCA 2D')
plt.legend()
plt.show()

if len(variaveisNumericas) >= 3 :
    # PCA para 3 componentes para o gráfico 3D
    pca3d = PCA(n_components=3)
    pca3dComponents = pca3d.fit_transform(pcaDataframeNormalizado)

    # Gráfico 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    for coluna, color in color_map.items():
        ax.scatter(pca3dComponents[colunaFiltrada == coluna, 0],
                pca3dComponents[colunaFiltrada == coluna, 1],
                pca3dComponents[colunaFiltrada == coluna, 2],
                label=coluna, color=color)
    ax.set_xlabel('Componente Principal 1')
    ax.set_ylabel('Componente Principal 2')
    ax.set_zlabel('Componente Principal 3')
    ax.set_title('PCA 3D')
    ax.legend()
    plt.show()
