import os, random
import matplotlib.pyplot as plt
import pandas as pd


def TT(a):
    address="./"+a
    ADD=random.choice(os.listdir(address))
    
    df_1=pd.read_csv(a+"/"+ADD)
    for i in range(0,12):
        plt.subplot(3,4,i+1)
        plt.plot(df_1.iloc[:,i])
        
        plt.xlim(0,1000) # 지저분해보여서 범위를 지정 ㅋ
        
    plt.show()

AA = [ 'SB', 'SI', 'AVNRT', 'ST', 'SAAWR', 'AT', 'SVT', 'AF', 'AFIB', 'AVRT', 'SR']
for j in range(11): # 11 == len(AA)
    TT(AA[j])
    
    
    

