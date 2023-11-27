import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("./data/over_one_mil_chars.csv")
data = data.rename(columns={"stats_1": "s_strength", "stats_2": "s_dexterity", "stats_3": "s_constitution", "stats_4": "s_intelligence", "stats_5": "s_wisdom", "stats_6": "s_charisma"})

cols_to_keep = ["name", "base_hp", "s_strength", "s_dexterity", "s_constitution", "s_intelligence", "s_wisdom", "s_charisma", "background", "race", "class_starting", "subclass_starting", "total_level", "notes_len"]

filtered_data = data[data["name"] != "Test"]
filtered_data = filtered_data[filtered_data["race"].notnull()]
filtered_data = filtered_data[filtered_data["background"].notnull()]
filtered_data = filtered_data[filtered_data["class_starting"].notnull()]
filtered_data = filtered_data[filtered_data["base_hp"] > 0]
filtered_data = filtered_data[filtered_data["s_strength"] > 0]
filtered_data = filtered_data[filtered_data["s_dexterity"] > 0]
filtered_data = filtered_data[filtered_data["s_constitution"] > 0]
filtered_data = filtered_data[filtered_data["s_intelligence"] > 0]
filtered_data = filtered_data[filtered_data["s_wisdom"] > 0]
filtered_data = filtered_data[filtered_data["s_charisma"] > 0]
filtered_data = filtered_data[filtered_data["total_level"] <= 20]

#print(len(filtered_data))

filtered_data = filtered_data[cols_to_keep]

filtered_data.to_csv("./data/dndData.csv")