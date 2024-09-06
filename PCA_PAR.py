import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import argparse
import json
from time import time

# CRIA O ARQUIVO .json COM OS PARAMETROS DE INPUT
def criarArquivoPars(filePath):
    
    parametros = {
        "coluna_de_categorias":"LITO",
        "codigos_das_categorias":[
            "IC",
            "IGO",
            "IF",
            "IFR",
	        "HF",
	        "HGO",
        ],
        "variaveis_numericas_de_analise":[
            "feglc",
            "mgglc",
            "alglc",
            "caglc",
            "pglc",
            "foglc",
            "siglc",	
        ],
        "codigo_valor_nao_atibuido":"-99.00",
        "CSV_delimiter":";"
    }
        
    # Escrevendo o DataFrame para um arquivo JSON com formatação
    with open(filePath, "w") as json_file:
        json.dump(parametros, json_file, indent=4)
    
    print("Arquivo parametros.json criado com sucesso.")
    
# LÊ O ARQUIVO .json COM OS PARAMETROS DE INPUT
def lerArquivoPars(filePath):
    try:
        with open("./" + filePath, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"O arquivo {filePath} não foi encontrado.")
        exit(1)
    except json.JSONDecodeError:
        print(f"O arquivo {filePath} não é um JSON válido.")
        exit(1)
        
# DEFINE OS PARÂMETROS DE INPUT
parser = argparse.ArgumentParser(description="Principal Component Analyses")
parser.add_argument("-P","--pars", type=str, help="Caminho do arquivo de parâmetros JSON") 
parser.add_argument("-A","--assay", type=str, help="Caminho do arquivo assay")
args = parser.parse_args()

print(f'\n {args}',"\n")

# Se o parametro --assay não for informado, um arquivo parametros.json será criado no local especificado
if args.pars and not args.assay:
    criarArquivoPars(args.pars)
    exit(1)

# Lê o arquivo parametros.json
PARS = lerArquivoPars(args.pars)
COLUNA_CATEGORIAS = PARS["coluna_de_categorias"]
CODIGOS_CATEGORIAS = PARS["codigos_das_categorias"]
VARIAVEIS_NUMERICAS = PARS["variaveis_numericas_de_analise"]
NA_VALUES_CODE = PARS["codigo_valor_nao_atibuido"]
CSV_DELIMITER = PARS["CSV_delimiter"]
print(
    f' coluna_de_categorias: {COLUNA_CATEGORIAS}\n', 
    f'codigos_das_categorias: {CODIGOS_CATEGORIAS}\n',
    f'variaveis_numericas_de_analise: {VARIAVEIS_NUMERICAS}\n',
    f'codigo_valor_nao_atibuido: {NA_VALUES_CODE}\n',
    f'CSV_delimiter: {CSV_DELIMITER}\n',
    )

# FILE recebe o caminho do arquivo assay
ASSAY_PATH = args.assay

# Lê o arquivo assay
assay = pd.read_csv(ASSAY_PATH, na_values=NA_VALUES_CODE, delimiter=CSV_DELIMITER)

# Filtra o assay em relação as categorias informadas
assay = assay[assay[COLUNA_CATEGORIAS].isin(CODIGOS_CATEGORIAS)]

# Filtra o assay em relação ao codigo de valores não atribuidos
pcaData = assay[VARIAVEIS_NUMERICAS].dropna()

# Padronização dos dados
scaler = StandardScaler()
pcaDataframeNormalizado = scaler.fit_transform(pcaData)

# Preparar os dados de cores das categorias após a filtragem
colunaFiltrada = assay[COLUNA_CATEGORIAS][pcaData.index]

# Crie um mapeamento de códigos de categorias para atribuir as cores
colunaItens = colunaFiltrada.unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(colunaItens)))
color_map = dict(zip(colunaItens, colors))

# PCA para 2 componentes para o gráfico 2D
pca2d = PCA(n_components=2)
pca2dComponents = pca2d.fit_transform(pcaDataframeNormalizado)

# Gráfico 2D
plt.figure(figsize=(8, 6))
for categorias, color in color_map.items():
    plt.scatter(pca2dComponents[colunaFiltrada == categorias, 0],
                pca2dComponents[colunaFiltrada == categorias, 1],
                label=categorias, color=color)
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.title("PCA 2D")
plt.legend()

# PCA para 3 componentes para o gráfico 3D
pca_3d = PCA(n_components=3)
principal_components_3d = pca_3d.fit_transform(pcaDataframeNormalizado)

# Gráfico 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
for categorias, color in color_map.items():
    mask = (colunaFiltrada == categorias)
    ax.scatter(principal_components_3d[mask, 0],
               principal_components_3d[mask, 1],
               principal_components_3d[mask, 2],
               label=categorias, color=color)
ax.set_xlabel("Componente Principal 1")
ax.set_ylabel("Componente Principal 2")
ax.set_zlabel("Componente Principal 3")
ax.set_title("PCA 3D")
ax.legend()

# Mostra os dois gráficos
plt.show()
