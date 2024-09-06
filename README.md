# Análise de Componentes Principais (PCA)

## Introdução


A Análise de Componentes Principais (PCA) é uma técnica de  redução de dimensionalidade e decorrelação de dados multivariados. Transforma uma distrubuição multivariada correlacionada em uma combinação linear ortogonal das variáveis originais. A técnica é de grande utilidade na geoestatística pelas seguintes rasões:

1. Dados multivariados, consistindo em várias variáveis geológicas correlacionadas, são transformados por PCA para se tornarem não correlacionados. A modelagem geoestatística independente das variáveis decorrelacionadas então prossegue, antes que a retrotransformação do PCA restaure a correlação original às variáveis modeladas.

2. PCA pode ser usado para redução de dimensionalidade no contexto acima. A modelagem geoestatística independente prossegue em um subconjunto das variáveis decorrelacionadas, antes que a retrotransformação do PCA forneça modelos de todas as variáveis originais.

Fonte: [BARNETT, Ryan M. Principal component analysis. Geostatistics Lessons; Deutsch, JL, 2017.](https://geostatisticslessons.com/pdfs/principalcomponentanalysis.pdf)

## Sumário


- [Introdução](#introdução)
- [Como o algorítimo funciona](#como-o-algorítimo-funciona)
- [Requesitos](#requesitos)
- [Como utilizar este programa](#como-utilizar-este-programa)
- [Exemplo de uso](#exemplo-de-uso)

## Como o algorítimo funciona
  

O algorítimo funciona da seguinte forma:

1.  **Definição de Parâmetros**: Cria ou lê um arquivo JSON com parâmetros de entrada.
2.  **Leitura de Dados**: Lê o arquivo de dados e filtra por categorias especificadas.
3.  **Padronização**: Padroniza os dados numéricos usando StandardScaler.
4.  **PCA**: Aplica PCA para reduzir a dimensionalidade dos dados.
5.  **Visualização**: Gera gráficos 2D e 3D dos componentes principais.


## Requesitos


* Python 3.x
* Bibliotecas: `Sklearn`, `Pandas`, `Numpy`, `Matplotlib`, `Argparse`, `Json`, `Time`


## Como utilizar este programa


1. Instale as dependências:
    ```bash
    pip install scikit-learn pandas matplotlib argparse json

2. Execute o script via linha de comando
    ```bash
    python nome_do_script.py -P caminho/arquivo/pars.json -A caminho/arquivo/assay.csv

* `-P` ou `--pars`: Cria um arquivo JSON (se usado sem outros argumentos) ou lê um arquivo JSON do local especificado para inserir valores de entrada.
* `-A` ou `--assay`: Especifica o caminho e nome do arquivo assay (*.csv) contendo os dados de entrada.


## Exemplo de uso


1. Gere um arquivo json de parametros: <code>python PCA_PAR.py -P pars.json</code>

3. Preencha o arquivo de parâmetros

2. Execute o script informando o arquivo de parametros e o de intervalos: <code>python PCA_PAR.py -P pars.json -A assay.csv</code>
  



