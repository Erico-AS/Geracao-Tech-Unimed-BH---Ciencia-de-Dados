# -*- coding: utf-8 -*-
"""Python_Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aGpTYbIOzCXjMhkzLdRAPXtBFKqjGfJI

# **Python com Pandas**
"""

#Importar bíblioteca
import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/datasets/Gapminder.csv", error_bad_lines=False, sep=";")

#5 primeiras linhas
df.head()

#Renomeando para portugues as colunas
df.rename(columns={"country": "País", "continent": "Continente", "year": "Ano", "lifeExp": "Expec. de vida", "gdpPercap": "Renda PerCapita"})

#Renomeando de fato
df = df.rename(columns={"country": "País", "continent": "Continente", "year": "Ano", "lifeExp": "Expec. de vida", "gdpPercap": "Renda PerCapita"})

#Linhas, colunas
df.shape

#Ver colunas
df.columns

#Ver tipos das colunas
df.dtypes

#Dados estatísticos da base de dados
df.describe()

#Ultimas linhas
df.tail()

#Fazer um filtro
df["Continente"].unique()
# [Coluna].retorne valores unicos da coluna

#Atribuir uma tabela com resultados de onde "Continente" == "Oceania"
Oceania = df.loc[df["Continente"] == "Oceania"]
#Var = localizar onde "Continente" == "Oceania"

#Mostra 5 primeiras linhas da tabela com "Continente" == "Oceania"
Oceania.head(5)

df.groupby("Continente")["País"].nunique()
  #agrupe por (coluna para agrupamento)["Colunas agrupadas"].contagem distinta

#Média da Expec. de vida para cada país
df.groupby("País")["Expec. de vida"].mean()
# mean = média