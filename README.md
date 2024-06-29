# Análise de Componentes Principais (PCA)


## Introdução


A Análise de Componentes Principais (PCA) em geoestatística é usada para reduzir a dimensionalidade dos dados espaciais, identificando as variáveis mais importantes que explicam a maior parte da variação nos dados. Isso facilita a visualização e interpretação das relações espaciais e padrões geográficos complexos.

## Sumário


- [Introdução](#introdução)
- [Como o algorítimo funciona](#como-o-algorítimo-funciona)
- [Libraries](#libraries)
- [Como utilizar este programa](#como-utilizar-este-programa)
- [Exemplo de uso](#exemplo-de-uso)

## Como o algorítimo funciona
  

O algorítimo funciona da seguinte forma:

1.  **Instalação de Pacotes**: Verifica e instala pacotes necessários usando pip.
2.  **Definição de Parâmetros**: Cria ou lê um arquivo JSON com parâmetros de entrada.
3.  **Leitura de Dados**: Lê o arquivo de dados e filtra por categorias especificadas.
4.  **Padronização**: Padroniza os dados numéricos usando StandardScaler.
5.  **PCA**: Aplica PCA para reduzir a dimensionalidade dos dados.
5.  **Visualização**: Gera gráficos 2D e 3D dos componentes principais.


## Libraries


1.  **Sklearn**
2.  **Pandas**
3.  **Numpy**
4.  **Matplotlib**
5.  **Argparse**
6.  **Json**
7.  **Time**

## Como utilizar este programa


Este programa utiliza os seguintes argumentos como entrada para execução:

- **--pars (-p):** Cria um arquivo JSON (se usado sem outros argumentos) ou lê um arquivo JSON do local especificado para inserir valores de entrada.
- **--shl (-s):** Especifica o caminho e nome do arquivo assay (*.csv) contendo os dados de entrada.


## Exemplo de uso

1. **Criação do arquivo de parâmetros:**  <code>python PCA_PARS.py --pars pars.json</code> 

2. **Execução da análise:** <code>python PCA_PARS.py --pars pars.json --assay assay.csv</code>
  



