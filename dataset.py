
import pandas as pd

cnt=pd.read_csv('Emotions.csv',encoding='cp1252')
disp=cnt.info()
print(disp)

print('Emotions:',pd.unique(cnt['Emotion']))

