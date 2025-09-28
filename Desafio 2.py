# Desafio 2


import numpy as np
import pandas as pd

# ---- Importação do conjunto de dados

PL_24_25 = pd.read_csv('D:/Neto/Cursos/Estatística/4º Semestre/Introdução ao Python para Ciência de Dados/desafios/desafio 2/E0.csv')

# ---- Preparação dos Dados

# M. Times mandantes

df_Mand = PL_24_25[['HomeTeam', 'HY']].copy()
df_Mand.columns = ['Team', 'YellowCards']

# V. Times visitantes

df_Vis = PL_24_25[['AwayTeam', 'AY']].copy()
df_Vis.columns = ['Team', 'YellowCards']

# C. Combinando o total de cartões dos times

df_total_cartoes = pd.concat([df_Mand, df_Vis]) \
                     .groupby('Team')['YellowCards'].sum() \
                     .reset_index() # rodar tudo junto
                     
# A. Array numpy

cartoes = df_total_cartoes['YellowCards'].values

# ---- Análise em Numpy

## Média



## Variância Amostral



## Desvio Padrão

## Máximo

## Mínimo

## Quartis

### Desvio Interquartílico

### Coeficiente de Variação

### Assimetria


# ---- Análise em Pandas


## Média

mediaP = cartoes.mean()
print(mediaP)

## Variância Amostral

varP = cartoes.var()
print(varP)

## Desvio Padrão

stdP = cartoes.std()
print(stdP)

## Máximo

maxP = cartoes.max()
print(maxP)

## Mínimo

minP = cartoes.min()
print(minP)

## Quartis

cartoesPD = df_total_cartoes['YellowCards']

quartis = cartoesPD.quantile([0.25, 0.5, 0.75])

print(quartis[0.25])
print(quartis[0.50])
print(quartis[0.75])

### Desvio Interquartílico

q1PD = quartis[0.25]
q3PD = quartis[0.75]

iqrPD = q3PD - q1PD
print(iqrPD)

### Coeficiente de Variação

cv_pandas = (stdP / mediaP) * 100
print(cv_pandas)

### Assimetria

assimPD = cartoesPD.skew()
print(assimPD)
