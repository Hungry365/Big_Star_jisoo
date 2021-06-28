import pandas as pd
import shutil
import matplotlib as plt

df = pd.read_excel("Diagnostics.xlsx")

df = df[['FileName', 'Rhythm']]


i = 0

for i in range(len(df)):
    
    if (df.iloc[i,1] == "SB"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./SB")

    elif (df.iloc[i,1] == "SR"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./SR")   
        
    elif (df.iloc[i,1] == "AFIB"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./AFIB")         
    
    elif (df.iloc[i,1] == "ST"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./ST")         
    
    elif (df.iloc[i,1] == "AF"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./AF")         
    
    elif (df.iloc[i,1] == "SA"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./SI")         
    
    elif (df.iloc[i,1] == "SVT"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./SVT")         
    
    elif (df.iloc[i,1] == "AT"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./AT")  
        
    elif (df.iloc[i,1] == "AVNRT"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./AVNRT")  
        
    elif (df.iloc[i,1] == "AVRT"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./AVRT")         
    
    elif (df.iloc[i,1] == "SAAWR"):
        shutil.copy("./ECGDataDenoised/"+df.iloc[i,0]+".csv","./SAAWR")       
        

    
      
    
    
    
