
import time
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score



def Testing(model, file):
	
	test_ = pd.read_csv(file,   encoding='cp1252')
	Y=test_['Emotion']
	p_model = pickle.load(open(model, 'rb'))
	predicted_class = p_model.predict(test_['Statement'])
	accuracy = accuracy_score(Y, predicted_class)
	precision = precision_score(Y, predicted_class, pos_label='joy', average='weighted')
	recall = recall_score(Y, predicted_class, pos_label='joy', average='weighted')
	fscore = f1_score(Y, predicted_class, pos_label='joy', average='micro')
	accuracy=round(accuracy,3)
	precision=round(precision,3)
	recall=round(recall,3)
	fscore=round(fscore,3)
	d=(accuracy, precision, recall,fscore)
	return d 


if __name__ == '__main__':
	Testing('knn_model.sav','Testingdata.csv')