import pandas as pd
import matplotlib.pyplot as plt
import os, random


def Plot(a):
    file = random.choice(os.listdir("./"+a))
    file_1=pd.read_csv("./"+a+"/"+file)
    for i in range(0,12):
        
        plt.subplot(3,4,i+1)    
        plt.title(a)
        plt.plot(file_1.iloc[:,i])
        plt.xlim(0,1000)
        
    
    plt.show()


Rhythms=['AF','AFIB','AT','AVNRT','SA','SAAWR','SB','SR','ST','SVT','AVRT']
for j in range(len(Rhythms)):
    Plot(Rhythms[j])
    print(j)
    
    




