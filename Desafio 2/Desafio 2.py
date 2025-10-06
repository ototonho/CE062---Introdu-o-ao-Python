# Desafio 2


import numpy as np
import pandas as pd
from scipy.stats import skew 

# ---- Importação do conjunto de dados

PL_24_25 = pd.read_csv('D:/Neto/Cursos/Estatística/4º Semestre/Introdução ao Python para Ciência de Dados/desafios/desafio 2/E0.csv')

# ---- Preparação dos Dados

# M. Times mandantes

df_Mand = PL_24_25.groupby('HomeTeam')['HY'].sum().reset_index()
df_Mand.columns = ['Team', 'Home_YellowCards']

# V. Times visitantes 

df_Vis = PL_24_25.groupby('AwayTeam')['AY'].sum().reset_index()
df_Vis.columns = ['Team', 'Away_YellowCards']

# C. Combinando o total de cartões dos times

df_Mand_temp = PL_24_25[['HomeTeam', 'HY']].copy()
df_Mand_temp.columns = ['Team', 'YellowCards']
df_Vis_temp = PL_24_25[['AwayTeam', 'AY']].copy()
df_Vis_temp.columns = ['Team', 'YellowCards']
df_total_cartoes = pd.concat([df_Mand_temp, df_Vis_temp]) \
                     .groupby('Team')['YellowCards'].sum() \
                     .reset_index()
                     
df_total_cartoes.columns = ['Team', 'Total_YellowCards']

cartoes_merged = pd.merge(df_Mand, df_Vis, on='Team', how='outer')
cartoes_merged = pd.merge(cartoes_merged, df_total_cartoes, on='Team', how='outer')
                     
# A. Array numpy

cartoes = cartoes_merged['Total_YellowCards'].values
cartoes_mandante = cartoes_merged['Home_YellowCards'].values
cartoes_visitante = cartoes_merged['Away_YellowCards'].values

# ---- Análise em Numpy

## Função 1 - média, variância e desvio padrão

print("FUNÇÃO 1: Média, Variância e Desvio Padrão (Numpy)")

def medidas_tendencia_dispersao(arr):
  media = np.mean(arr)
  variancia_amostral = np.var(arr, ddof=1)
  desvio_padrao_amostral = np.std(arr, ddof=1)
  
  return media, variancia_amostral, desvio_padrao_amostral

media, variancia, desvio_padrao = medidas_tendencia_dispersao(cartoes_mandante)
print("Função 1: Média, Variância e Desvio Padrão")
print(f"Média: {media:.4f}")
print(f"Variância Amostral: {variancia:.4f}")
print(f"Desvio Padrão Amostral: {desvio_padrao:.4f}\n")

media, variancia, desvio_padrao = medidas_tendencia_dispersao(cartoes_visitante)
print("Função 1: Média, Variância e Desvio Padrão")
print(f"Média: {media:.4f}")
print(f"Variância Amostral: {variancia:.4f}")
print(f"Desvio Padrão Amostral: {desvio_padrao:.4f}\n")

media, variancia, desvio_padrao = medidas_tendencia_dispersao(cartoes)
print("Função 1: Média, Variância e Desvio Padrão")
print(f"Média: {media:.4f}")
print(f"Variância Amostral: {variancia:.4f}")
print(f"Desvio Padrão Amostral: {desvio_padrao:.4f}\n")

## Função 2 - máx, mín, quartis

print("FUNÇÃO 2: Máximo, Mínimo, Quartis e IIQ (Numpy)")

def medidas_posicao_quartis(arr):
    
    # Máximo e Mínimo
    maximo = np.max(arr)
    minimo = np.min(arr)
    
    # Quartis: np.percentile(arr, [25, 50, 75]) - Q1, Q2 (Mediana) e Q3
    q1, q2_mediana, q3 = np.percentile(arr, [25, 50, 75])
    
    # Desvio Interquartílico (IIQ) é a diferença entre Q3 e Q1
    iiq = q3 - q1
    
    return {
        "Máximo": maximo,
        "Mínimo": minimo,
        "Q1 (25%)": q1,
        "Q2 (Mediana/50%)": q2_mediana,
        "Q3 (75%)": q3,
        "Desvio Interquartílico (IIQ)": iiq
    }


resultados_quartis = medidas_posicao_quartis(cartoes_mandante)
print("Função 2: Máximo, Mínimo, Quartis e IIQ")
for chave, valor in resultados_quartis.items():
    print(f"{chave}: {valor:.4f}")
print()

resultados_quartis = medidas_posicao_quartis(cartoes_visitante)
print("Função 2: Máximo, Mínimo, Quartis e IIQ")
for chave, valor in resultados_quartis.items():
    print(f"{chave}: {valor:.4f}")
print()

resultados_quartis = medidas_posicao_quartis(cartoes)
print("Função 2: Máximo, Mínimo, Quartis e IIQ")
for chave, valor in resultados_quartis.items():
    print(f"{chave}: {valor:.4f}")
print()

## Função 3 - coeficiente de variação e assimetria

print("FUNÇÃO 3: Coeficiente de Variação e Assimetria (Numpy)")

def coeficiente_variacao_assimetria(arr):
    
    # Desvio Padrão Amostral (necessário para o CV)
    desvio_padrao_amostral = np.std(arr, ddof=1)
    
    # Média (necessário para o CV)
    media = np.mean(arr)
    
    # Coeficiente de Variação (CV): (Desvio Padrão / Média) * 100
    # Adiciono uma verificação para evitar divisão por zero, embora seja raro em dados reais.
    if media == 0:
        cv = np.nan
    else:
        cv = (desvio_padrao_amostral / media) * 100
        
    # Assimetria (Skewness): utiliza a função da biblioteca SciPy, recomendada para arrays NumPy
    # bias=False: Corrige o viés para amostras (ajustada para populações menores)
    assimetria = skew(arr, bias=False)
    
    return cv, assimetria

cv, assimetria = coeficiente_variacao_assimetria(cartoes_mandante)
print("Função 3: Coeficiente de Variação e Assimetria")
print(f"Coeficiente de Variação (CV): {cv:.4f}%")
print(f"Assimetria (Skewness): {assimetria:.4f}")

cv, assimetria = coeficiente_variacao_assimetria(cartoes_visitante)
print("Função 3: Coeficiente de Variação e Assimetria")
print(f"Coeficiente de Variação (CV): {cv:.4f}%")
print(f"Assimetria (Skewness): {assimetria:.4f}")

cv, assimetria = coeficiente_variacao_assimetria(cartoes)
print("Função 3: Coeficiente de Variação e Assimetria")
print(f"Coeficiente de Variação (CV): {cv:.4f}%")
print(f"Assimetria (Skewness): {assimetria:.4f}")

# ---- Análise em Pandas

cartoes_mandante_p = cartoes_merged['Home_YellowCards']
cartoes_visitante_p = cartoes_merged['Away_YellowCards']
cartoes_p = cartoes_merged['Total_YellowCards']

dados_pandas = {
    "Cartões Mandante": cartoes_mandante_p,
    "Cartões Visitante": cartoes_visitante_p,
    "Total Cartões": cartoes_p
}

## Função 1 - Média, Variância e Desvio Padrão (Pandas)

print("FUNÇÃO 1: Média, Variância e Desvio Padrão (Pandas)")

for nome, serie in dados_pandas.items():
    
    media = serie.mean()
    variancia = serie.var(ddof=1) 
    desvio_padrao = serie.std(ddof=1) 

    print(f"{nome}")
    print(f"Média: {media:.4f}")
    print(f"Variância Amostral: {variancia:.4f}")
    print(f"Desvio Padrão Amostral: {desvio_padrao:.4f}\n")

dados_pandas = {
    "Cartões Mandante": cartoes_mandante_p,
    "Cartões Visitante": cartoes_visitante_p,
    "Total Cartões": cartoes_p
}

## Função 2 - Máx, Mín, Quartis (Pandas)

print("FUNÇÃO 2: Máximo, Mínimo, Quartis e IIQ (Pandas)")

for nome, serie in dados_pandas.items():
    # .describe() no Pandas calcula a maioria dessas métricas de uma vez
    descritivo = serie.describe()
    
    maximo = descritivo['max']
    minimo = descritivo['min']
    q1 = descritivo['25%']
    mediana = descritivo['50%']
    q3 = descritivo['75%']
    iiq = q3 - q1

    print(f"{nome}")
    print(f"Máximo: {maximo:.4f}")
    print(f"Mínimo: {minimo:.4f}")
    print(f"Q1 (25%): {q1:.4f}")
    print(f"Q2 (Mediana/50%): {mediana:.4f}")
    print(f"Q3 (75%): {q3:.4f}")
    print(f"Desvio Interquartílico (IIQ): {iiq:.4f}\n")

dados_pandas = {
    "Cartões Mandante": cartoes_mandante_p,
    "Cartões Visitante": cartoes_visitante_p,
    "Total Cartões": cartoes_p
}

## Função 3 - Coeficiente de Variação e Assimetria (Pandas)

print("FUNÇÃO 3: Coeficiente de Variação e Assimetria (Pandas)")

for nome, serie in dados_pandas.items():
    media = serie.mean()
    desvio_padrao = serie.std(ddof=1)
    
    # Coeficiente de Variação (CV)
    if media == 0:
        cv = np.nan
    else:
        cv = (desvio_padrao / media) * 100
        
    # Assimetria (Skewness): .skew() nativo do pandas
    assimetria = serie.skew() 
    
    print(f"{nome}")
    print(f"Coeficiente de Variação (CV): {cv:.4f}%")
    print(f"Assimetria (Skewness): {assimetria:.4f}\n")
    
dados_pandas = {
    "Cartões Mandante": cartoes_mandante_p,
    "Cartões Visitante": cartoes_visitante_p,
    "Total Cartões": cartoes_p
}
