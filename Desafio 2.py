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

def mediaN(cartoes):
  somaN = np.sum(cartoes)
  nN = cartoes.size
  media = somaN / nN
  return media

print(mediaN(cartoes))

mediaN = np.sum(cartoes) / cartoes.size
print(mediaN)

## Variância Amostral

def varN(cartoes):
  mv = mediaN(cartoes)
  desvios_quad = np.power(cartoes - mv, 2)
  soma_desvios = np.sum(desvios_quad)
  nv = cartoes.size
  var = soma_desvios / (nv - 1)
  return var

print(varN(cartoes))

## Desvio Padrão

def stdN(cartoes):
  v = varN(cartoes)
  desv = np.sqrt(v)
  return desv

print(stdN(cartoes))

## Máximo

def maxN(cartoes):
  array_ordenado = np.sort(cartoes)
  return array_ordenado[-1]

print(maxN(cartoes))

## Mínimo

def minN(cartoes):
  array_ordenado = np.sort(cartoes) 
  return array_ordenado[0]

print(minN(cartoes))

## Quartis

def quartisN(array):
    """Calcula Q1 (25%), Mediana/Q2 (50%) e Q3 (75%) com interpolação."""
    
    dados_ordenados = np.sort(array)
    n = dados_ordenados.size
    
    # Esta é a função interna. Ela PRECISA ser definida AQUI.
    def calcular_quartil(p):
        L = (p / 100) * (n - 1) # Posição do índice (base 0)
        i = int(L)
        f = L - i
        
        # O bloco IF deve ter indentação correta
        if i >= n - 1:
            return dados_ordenados[n - 1]
        
        # Interpolação Linear
        return dados_ordenados[i] + f * (dados_ordenados[i+1] - dados_ordenados[i])

    # Chamadas finais, com a indentação correta (dentro de quartisN)
    q1 = calcular_quartil(25)
    mediana = calcular_quartil(50)
    q3 = calcular_quartil(75)
    
    return q1, mediana, q3


q1_np, mediana_np, q3_np = quartisN(cartoes)
print(q1_np)
print(mediana_np)
print(q3_np)

### Desvio Interquartílico

def iqrN(array):
    q1, _, q3 = quartisN(array)
    return q3 - q1

print(iqrN(cartoes))

### Coeficiente de Variação

def cvN(cartoes):
    media = mediaN(cartoes)
    desvio_padrao = stdN(cartoes)
    
    if media == 0:
        return 0
    
    return (desvio_padrao / media) * 100
  
print(cvN(cartoes))

### Assimetria

def skewN(cartoes):
    
    mu = mediaN(cartoes)
    sigma = stdN(cartoes)
    n = cartoes.size
    
    if n < 3:
        return 0
    
    # Z-scores: (xi - mu) / sigma
    z_scores = (cartoes - mu) / sigma
    
    # Soma dos cubos dos Z-scores
    soma_cubos = np.sum(np.power(z_scores, 3))
    
    # Fator de correção para a amostra
    fator_correcao = n / ((n - 1) * (n - 2))
    
    return fator_correcao * soma_cubos
  
print(skewN(cartoes))

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
