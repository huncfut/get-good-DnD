import pandas as pd

convertToNumber = False
data = pd.read_csv("./data/over_one_mil_chars.csv")
data = data.rename(columns={"stats_1": "s_str", "stats_2": "s_dex", "stats_3": "s_con", "stats_4": "s_int", "stats_5": "s_wis", "stats_6": "s_cha"})

cols_to_keep = ["name", "base_hp", "s_str", "s_dex", "s_con", "s_int", "s_wis", "s_cha", "background", "race", "class_starting", "subclass_starting", "total_level", "notes_len"]

filtered_data = data[data["name"] != "Test"]
filtered_data = filtered_data[filtered_data["race"].notnull()]
filtered_data = filtered_data[filtered_data["background"].notnull()]
filtered_data = filtered_data[filtered_data["class_starting"].notnull()]
filtered_data = filtered_data[filtered_data["base_hp"] > 0]
filtered_data = filtered_data[filtered_data["s_str"] > 0]
filtered_data = filtered_data[filtered_data["s_dex"] > 0]
filtered_data = filtered_data[filtered_data["s_con"] > 0]
filtered_data = filtered_data[filtered_data["s_int"] > 0]
filtered_data = filtered_data[filtered_data["s_wis"] > 0]
filtered_data = filtered_data[filtered_data["s_cha"] > 0]
filtered_data = filtered_data[filtered_data["total_level"] <= 20]
filtered_data = filtered_data[filtered_data["notes_len"] > 0]
filtered_data = filtered_data[filtered_data["total_level"] > 1]

filtered_data = filtered_data[cols_to_keep]
filtered_data = filtered_data.replace(["Blood Hunter (archived)", "Artificer (UA)"], ["Blood Hunter", "Artificer"])

filtered_data.to_csv("./data/dndDataStripped.csv", index=False)