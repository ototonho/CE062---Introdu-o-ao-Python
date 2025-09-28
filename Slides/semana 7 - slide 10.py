import pandas as pd
import numpy as np

df = pd.read_csv('cursosMariaDB.csv')
print(df.head()) # visualizar o início da tabela

df.columns = ['Ano','Curso','Turno','Duração','Vagas','Inscritos','Ingressantes','Matriculados','Concluintes'] # corrigindo o nome das colunas
View(df)

matriculados = df['Matriculados'].to_numpy() # transforma em objeto a ser manipulado pelo numpy
concluintes = df['Concluintes'].to_numpy()


print("Máximo de Concluintes: ", np.max(concluintes))
print("Média de matriculados: ", np.mean(matriculados))

df['Taxa de conclusão'] = (df['Concluintes'] / df['Ano'])

df.groupby('Curso')[['Taxa de conclusão']].mean()

