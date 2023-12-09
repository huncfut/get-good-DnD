import pandas as pd
import numpy as np
import warnings
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

warnings.filterwarnings("ignore")

stats = ["s_str", "s_dex", "s_con", "s_int", "s_wis", "s_cha"]
stats_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charmisma"]
data = pd.read_csv("./data/proportionalDataStripped.csv")

downsized_stats = pd.DataFrame(columns=["s_str", "s_dex", "s_con", "s_int", "s_wis", "s_cha", "class_starting"])
for c in data["class_starting"].unique():
    sample = data[data["class_starting"] == c].sample(n=50000, random_state=2137, replace=True)
    downsized_stats = downsized_stats.append(sample)

X_train, X_test, y_train, y_test = train_test_split(np.array(downsized_stats[stats]), np.array(downsized_stats["class_starting"]), random_state=2137, test_size=0.2)

clf = tree.DecisionTreeClassifier(max_depth=28)
clf.fit(X_train, y_train)
y_predict = clf.predict(X_train)
train_acc = accuracy_score(y_train, y_predict)
y_predict = clf.predict(X_test)
test_acc = accuracy_score(y_test, y_predict)

print("Train Accuracy: " + str(train_acc) + " Test Accuracy: " + str(test_acc))

vals = []
for s in stats_names:
    vals.append(int(input("Enter " + s + ": ")))

val_acc = clf.predict([vals / np.max(vals)])
print("Best Class: ", val_acc[0])