import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize
from scipy import special
import sys, os


#definisco funzioni
def efficienza(df):
    ''' prende dati da file csv: int2 e int3 e calcolola l'efficienza e l'errore sull'efficienza '''
    tensione = np.array(df['tensione'])
    int2 = np.array(df['intersezione2'])
    int3 = np.array(df['intersezione3'])
    eff = int3/int2
    effErr= np.sqrt(eff*(1-eff)/int3)
    return tensione, eff, effErr

def errorFunction(x, mu, sigma, norm):
    x2 = (x-mu)/(np.sqrt(2)*sigma)
    return norm*(1 + special.erf(x2))/2


#importo dati da file csv
b2EffDf = pd.read_csv('b2Efficienza.csv')
tens2, eff2, effErr2 = efficienza(b2EffDf)

#definisco parametri ottimali (li abbiamo visti dal grafico e messi a caso)
mu = 1350
sigma = 65
norm = eff2[np.argmax(eff2)]
pstart = np.array([mu, sigma, norm])

#faccio il fit e trovo parametri ottimali
parametri, cov = optimize.curve_fit(errorFunction, tens2, eff2, p0=[pstart])
errParametri = np.sqrt(np.diag(cov))
print('parametri ottimali trovati: \n', 'mu: ', parametri[0],' ± ', errParametri[0], '\n sigma: ', parametri[1],' ± ', errParametri[1], '\n normalizzazione: ',parametri[2],' ± ', errParametri[2])

#ricalcolo valori con parametri ottimali
errFuncFit = errorFunction(tens2, parametri[0], parametri[1], parametri[2])

#faccio grafico fit e dati originali
plt.errorbar(tens2, eff2, yerr = effErr2,  fmt = '-o', color = 'rebeccapurple', label = 'dati originali', alpha = 0.8)
plt.plot(tens2, errFuncFit, color = 'green', alpha = 0.8, label = 'fit')
plt.grid()
plt.title('Fit vs dati originali')
plt.xlabel('tensione [mV]')
plt.ylabel('efficienza')
plt.legend()
plt.show()

#salvoParametri su file
d = {'parametri': parametri, 'errori': errParametri}

tabella = pd.DataFrame(data=d, index=['mu', 'sigma', 'normalizzazione'])
print(tabella)

currentDirectory = os.getcwd()
tabella.to_csv(currentDirectory+'/parametriFit')
