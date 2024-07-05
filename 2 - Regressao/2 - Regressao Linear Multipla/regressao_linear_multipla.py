# -*- coding: utf-8 -*-
"""regressao-linear-multipla.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10CVoPIG1RzGy-UGIj695X5rkSiT8E9XP

# Regressão linear múltipla

## Base preço das casas - MAE 123.888, 0.68
"""

base_casas

X_casas = base_casas.iloc[:, 3:19].values
X_casas

y_casas = base_casas.iloc[:, 2].values
y_casas

from sklearn.model_selection import train_test_split
X_casas_treinamento, X_casas_teste, y_casas_treinamento, y_casas_teste = train_test_split(X_casas, y_casas, test_size = 0.3, random_state = 0)

X_casas_treinamento.shape, X_casas_teste.shape

regressor_multiplo_casas = LinearRegression()
regressor_multiplo_casas.fit(X_casas_treinamento, y_casas_treinamento)

regressor_multiplo_casas.intercept_

regressor_multiplo_casas.coef_

len(regressor_multiplo_casas.coef_)

regressor_multiplo_casas.score(X_casas_treinamento, y_casas_treinamento)

regressor_multiplo_casas.score(X_casas_teste, y_casas_teste)

previsoes = regressor_multiplo_casas.predict(X_casas_teste)
previsoes

y_casas_teste

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_casas_teste, previsoes)