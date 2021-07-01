# 1.파형별 폴더 저장
import pandas as pd
import shutil

df = pd.read_excel('../data to go/Diagnostics.xlsx')
find_sig = df['Rhythm'] == 'AF' # 파형별로 바꿔가면서 출력

f = df[find_sig]
ff = f[['FileName']]

for i in range(len(ff)) :
    from_ = '../data to go/ECGDataDenoised/'+ff.values[i][0]+'.csv'
    to_='../심전도 분석/AF'  # 폴더도 파형별로 바꿔가면서 출력
    shutil.copy(from_,to_)