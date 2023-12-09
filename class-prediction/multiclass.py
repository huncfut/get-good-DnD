import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
import warnings

warnings.filterwarnings("ignore")

dataFile = "data/proportionalDataStripped.csv"
stats = ["s_str", "s_dex", "s_con", "s_int", "s_wis", "s_cha"]
stats_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charmisma"]
classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

data = pd.read_csv(dataFile)
data = data[data["class_starting"].isin(classes)]

X = data[stats]
y = data["class_starting"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2137, test_size=0.2)

# for layout in [[5], [10], [20], [5, 5], [5, 10], [10, 10], [20, 20], [5, 5, 5], [5, 10, 5]]:
#     model = OneVsRestClassifier(MLPClassifier(layout, activation="relu", random_state=2137), n_jobs=14).fit(X_train, y_train)
#     print(f'Training Accuracy: {accuracy_score(y_train, model.predict(X_train))}, Testing Accuracy: {accuracy_score(y_test, model.predict(X_test))}')

model = OneVsRestClassifier(MLPClassifier([50, 50], activation="relu", random_state=2137), n_jobs=14, verbose=100).fit(X_train, y_train)
print(f'Training Accuracy: {accuracy_score(y_train, model.predict(X_train))}, Testing Accuracy: {accuracy_score(y_test, model.predict(X_test))}')

# print(model.predict_proba([np.array(X_test)[0]]))
classes = model.classes_

while True:
    vals = []
    for s in stats_names:
        vals.append(int(input("Enter " + s + ": ")))

    best = model.predict([vals / np.max(vals)])
    multiclass = model.predict_proba([vals / np.max(vals)])[0]
    print(f'Best Class: {best}')
    print(classes[multiclass > 0.10])

    for i in range(len(classes)):
        print(f'  {classes[i]}: {multiclass[i]}')

