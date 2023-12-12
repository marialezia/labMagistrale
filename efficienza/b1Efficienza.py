import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#leggo dati da file csv
b1EffDf = pd.read_csv('b1Efficienza.csv')
tensione = np.array(b1EffDf['tensione'])
int2 = np.array(b1EffDf['intersezione2'])
int3 = np.array(b1EffDf['intersezione3'])

#calcolo efficienza ed errore efficienza
efficienza = int3/int2
effErr= np.sqrt(efficienza*(1-efficienza)/int3)

#faccio grafico
plt.errorbar(tensione, efficienza, yerr = effErr,  fmt = '-o')
plt.grid()
plt.xlabel('tensione [mV]')
plt.ylabel('efficienza')
plt.show()
