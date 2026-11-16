import pandas as pd
import numpy as np
import yfinance as yf

#Descarga de precios de Yahoo finance S&P500 , LATAM y Semiconductores (IA)
tickers = ["IVV","ILF","SOXX"] 
vector_w = [0.5, 0.3, 0.2] 
vector_w = np.array(vector_w).reshape(-1, 1)
df_prices = yf.download(tickers, start="2024-01-01" ,end = "2026-09-30")["Close"]
df_prices = df_prices[tickers]

#Calculo de retornos diarios

df_ret = df_prices.pct_change().dropna()

#Calculo de la matriz de covarianza

df_cov = df_ret.cov()
#print(df_cov)

#Calculo de varianza del portafolio

w = vector_w
w_t=w.T
sigma = df_cov.values

#print("w",w.shape)
#print("w_t",w_t.shape)
#print("sigma",sigma.shape)

varianza = np.dot(sigma,w) 
varianza = np.dot(w_t, varianza)[0][0]

desv = varianza**(1/2)
volatidad_anual = desv * (252**(1/2))
print(f"La volatilidad anual del portafolio es : {volatidad_anual*100:.04}%")

#Calculo de la media del portafolio

vector_ret = df_ret.mean()
vector_ret = vector_ret.values
vector_ret = vector_ret.reshape(-1, 1)
mu = np.dot(w_t, vector_ret)[0][0]
mu_anual = mu * 252
#print(f"La media anual del portafolio es :{mu_anual*100:.04}%")

#Calculo del Value at Risk (VaR) del portafolio al 95% de confianza 

var_95 = mu_anual - 1.64 * volatidad_anual
print(f"La VaR del portafolio es : {var_95*100:.04}%")

# FIRMA: BWoIyT3JkOMPjhfGXaEovQA5DoJrkvqbBCNzRNR5MOK6JZr_F-TIbhCdBUtAKuvwPZZI7Z5_8cJ0gYH1lGMKwAg4Y8jzJY22H_0O-Qi2h7hNuCM=
