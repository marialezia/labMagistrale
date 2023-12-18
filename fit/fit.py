import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize
from scipy import special

#importo dati da file csv
b2EffDf = pd.read_csv('b2Efficienza.csv')

def efficienza(df):
    tensione = np.array(df['tensione'])
    int2 = np.array(df['intersezione2'])
    int3 = np.array(df['intersezione3'])
    eff = int3/int2
    effErr= np.sqrt(eff*(1-eff)/int3)
    return tensione, eff, effErr

def errorFunction(x, mu, sigma):
    x2 = (x-mu)/(np.sqrt(2)*sigma)
    return (1 + special.erf(x2))/2

tens2, eff2, effErr2 = efficienza(b2EffDf)
mu = 1350
sigma = 65
erF = errorFunction(tens2, mu, sigma)
pstart = np.array([mu, sigma])
params, params_covariance = optimize.curve_fit(errorFunction, tens2, eff2, p0=[pstart])
print(params, params_covariance)
#plt.plot(tens2, errorFunction(eff2, 1))
#plt.plot(tens2, special.erf(tens2))
plt.plot(tens2, erF)
#plt.plot(tens2, errorFunction(tens2))
#plt.plot(tens2, special.erf(tens2))
plt.xlabel('$x$')

plt.ylabel('$erf(x)$')

plt.show()
