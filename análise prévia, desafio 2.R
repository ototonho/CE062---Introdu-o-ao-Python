# Análise prévia em R

library(tidyverse)
library(dplyr)

CartoesPL25 <- read.csv("D:/Neto/Cursos/Estatística/4º Semestre/Introdução ao Python para Ciência de Dados/desafios/desafio 2/E0.csv")

cartõesM <- CartoesPL25 %>%
  select(Time = HomeTeam, Cartoes_Amarelos = HY)
cartõesV <- CartoesPL25 %>%
  select(Time = AwayTeam, Cartoes_Amarelos = AY)

cartoes <- bind_rows(cartõesM, cartõesV) %>%
  group_by(Time) %>%
  summarise(CartõesAmarelos = sum(Cartoes_Amarelos, na.rm = TRUE)) %>%
  ungroup() %>%
  arrange(desc(CartõesAmarelos))

mean(cartoes$CartõesAmarelos)
var(cartoes$CartõesAmarelos)
sd(cartoes$CartõesAmarelos)

max(cartoes$CartõesAmarelos)
min(cartoes$CartõesAmarelos)
quantile(cartoes$CartõesAmarelos)

coef_var <- (sd(cartoes$CartõesAmarelos) / mean(cartoes$CartõesAmarelos)) * 100
print(coef_var)

install.packages("e1071")
library(e1071)

IQR(cartoes$CartõesAmarelos, na.rm = TRUE)
skewness(cartoes$CartõesAmarelos, na.rm = TRUE)
