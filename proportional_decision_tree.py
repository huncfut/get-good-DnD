import pandas as pd
import numpy as np
import os
import sys
from sklearn.model_selection import train_test_split


def transformCharacter(character):
  character.loc[stats] /= np.max(character[stats])
  return character[stats + ["class_starting"]]


dataFile = "data/proportionalData.csv"
stats = ["s_str", "s_dex", "s_con", "s_int", "s_wis", "s_cha"]


if(not os.path.exists(dataFile)):
  print(f'Creating the data file at "{dataFile}" – this may take a few minutes')

  pd.read_csv("data/dndData.csv") \
    .apply(transformCharacter, axis=1) \
    .to_csv(dataFile, index=False)
  
  print("File Created")


print(f'Reading "{dataFile}"')
df = pd.read_csv(dataFile)

# X_train, X_test, y_train, y_test = train_test_split(df[stats], df["class_starting"], random_state=2137, test_size=0.2)

# depth = sys.argv[1] if (len(sys.argv) > 1) else  & input("Depth to use: ")
