import pandas as pd
import numpy as np
import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
from sklearn import tree


def transformCharacter(character):
  character.loc[stats] /= np.max(character[stats])
  return character[stats + ["class_starting"]]

stats_names = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charmisma"]
dataFile = "data/proportionalDataStripped.csv"
stats = ["s_str", "s_dex", "s_con", "s_int", "s_wis", "s_cha"]


if(not os.path.exists(dataFile)):
  print(f'Creating the data file at "{dataFile}" – this may take a few minutes')

  pd.read_csv("data/dndDataStripped.csv") \
    .apply(transformCharacter, axis=1) \
    .to_csv(dataFile, index=False)
  
  print("File Created")


print(f'Reading "{dataFile}"')
df = pd.read_csv(dataFile)

X_train, X_test, y_train, y_test = train_test_split(df[stats], df["class_starting"], random_state=2137, test_size=0.2)

def runTree(depth, X_train, X_test, y_train, y_test):
  model = tree.DecisionTreeClassifier(max_depth=depth, random_state=2137).fit(X_train, y_train)
  

  print(f'Depth: {depth}')
  print(f'  Train: mean-squared = {ms_train}, R2 score = {r2_score_train}')
  print(f'  Test: mean-squared = {ms_test}, R2 score = {r2_score_test}')
  return model

def testDepths():
  X_sub, X_val, y_sub, y_val = train_test_split(X_train, y_train, random_state=2137, test_size=0.2)
  
  for d in range(1, 30):
    runTree(d, X_sub, X_val, y_sub, y_val)

  return input("Depth to use: ")

depth = int(sys.argv[1]) if (len(sys.argv) > 1) else testDepths()

runTree(depth, X_train, X_test, y_train, y_test)
