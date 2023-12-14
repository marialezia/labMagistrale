import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importo dati da file csv
b1EffDf = pd.read_csv('b1Efficienza.csv')
b2EffDf = pd.read_csv('b2Efficienza.csv')
b3EffDf = pd.read_csv('b3Efficienza.csv')

#definisco funzioni
def efficienza(df):
    tensione = np.array(df['tensione'])
    int2 = np.array(df['intersezione2'])
    int3 = np.array(df['intersezione3'])
    eff = int3/int2
    effErr= np.sqrt(eff*(1-eff)/int3)
    return tensione, eff, effErr

def plot(tensione, efficienza, errore, num):
    plt.errorbar(tensione, efficienza, yerr = errore,  fmt = '-o')
    plt.grid()
    plt.title('Efficienza B'+ num)
    plt.xlabel('tensione [mV]')
    plt.ylabel('efficienza')
    plt.show()

#calcolo efficienza ed errori 
tens1, eff1, effErr1 = efficienza(b1EffDf)
tens2, eff2, effErr2 = efficienza(b2EffDf)
tens3, eff3, effErr3 = efficienza(b3EffDf)

#faccio grafici
plot(tens1, eff1, effErr1, '1')
plot(tens2, eff2, effErr2, '2')
plot(tens3, eff3, effErr3, '3')

    
