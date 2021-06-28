import pandas as pd
import numpy as np
import os
import shutil

path = 'C:/Users/manci/Desktop/data to go/ECGDataDenoised'
Ecg_Data = pd.read_excel('Diagnostics.xlsx')
df = pd.DataFrame(Ecg_Data)
choose_data = df.iloc[:,:2]

j = 0

for j in range(len(choose_data)):
    if(choose_data.iloc[j,1] == 'SB'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\SB')
    elif(choose_data.iloc[j,1] == 'SR'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\SR')
    elif(choose_data.iloc[j,1] == 'AFIB'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\AFIB')
    elif(choose_data.iloc[j,1] == 'ST'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\ST')
    elif(choose_data.iloc[j,1] == 'AF'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\AF')
    elif(choose_data.iloc[j,1] == 'SA'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\SA')
    elif(choose_data.iloc[j,1] == 'SVT'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\SVT')        
    elif(choose_data.iloc[j,1] == 'AT'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\AT')
    elif(choose_data.iloc[j,1] == 'AVNRT'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\AVNRT')        
    elif(choose_data.iloc[j,1] == 'AVRT'):
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\AVRT')
    else:
        shutil.copy('C:/Users\manci\Desktop\data to go\ECGDataDenoised/'+choose_data.iloc[j,0]+'.csv',
                    'C:/Users\manci\Desktop\data to go\SAAWR')