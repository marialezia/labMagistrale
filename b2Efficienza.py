import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#leggo dati da file csv
b2EffDf = pd.read_csv('b2Efficienza.csv')
tensione = np.array(b2EffDf['tensione'])
int2 = np.array(b2EffDf['intersezione2'])
int3 = np.array(b2EffDf['intersezione3'])

#calcolo efficienza ed errore efficienza
efficienza = int3/int2
effErr= np.sqrt(efficienza*(1-efficienza)/int3)

#faccio grafico
plt.plot(tensione, efficienza, 'o-')
plt.grid()
plt.xlabel('tensione [mV]')
plt.ylabel('efficienza')
plt.show()
