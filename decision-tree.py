import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

stats = ["s_str", "s_dex", "s_con", "s_int", "s_wis", "s_cha"]
data = pd.read_csv("./data/dndData.csv")
X_train, X_test, y_train, y_test = train_test_split(np.array(data[stats], dtype='int'), np.array(data["class_starting"]), random_state=2137, test_size=0.2)

clf = tree.DecisionTreeClassifier(max_depth=29)
clf.fit(X_train, y_train)
y_predict = clf.predict(X_train)
train_acc = accuracy_score(y_train, y_predict)
y_predict = clf.predict(X_test)
test_acc = accuracy_score(y_test, y_predict)

vals = []
vals.append(input("Enter Strength: "))
vals.append(input("Enter Dexterity: "))
vals.append(input("Enter Constitution: "))
vals.append(input("Enter Intelligence: "))
vals.append(input("Enter Wisdom: "))
vals.append(input("Enter Charmisma: "))

val_acc = clf.predict([vals])
print("Best Class: ", val_acc[0])