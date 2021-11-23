import numpy as np
from sklearn.ensemble import RandomForestClassifier
def classifica(treino,classes,teste):
    clf = RandomForestClassifier(random_state=0)
    clf.fit(treino, classes)
    return clf.predict(teste)

