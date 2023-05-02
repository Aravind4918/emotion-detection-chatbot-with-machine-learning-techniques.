import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn import svm

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle


class NBTrain:

    def train():
        t_f = 'Emotions.csv'
        t_d = pd.read_csv(t_f, encoding='cp1252')
        tf_idf = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)  # TF-IDF
    
        pipeline = Pipeline([('TF_IDF', tf_idf), ('model', BernoulliNB())])

        model_name = 'nb_model.sav'
        pickle.dump(pipeline.fit(t_d['Statement'], t_d['Emotion']), open(model_name, 'wb'))

  

if __name__ == "__main__":
    pass
