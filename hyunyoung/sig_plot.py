# 2.랜덤으로 파형별 그래프 그리기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name = ['AF','AFIB','AT','AVNRT','AVRT','SAAWR','SB','SI','SR','ST','SVT']
num = np.random.randint(len(name))
file = pd.read_csv('../심전도 분석/data',num)

for i in range(len(name)):
    plt.subplot(3,4,i+1)       
    plt.figure()
    plt.plot(file.iloc[:,1])
    plt.title(name,num)

plt.show()