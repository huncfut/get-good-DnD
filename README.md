# Get Good DnD

A machine learning model by Harrison Hoytt, Christian Tongate, and Kuba Zeligowski for UTK's COSC 425: Intro to Machine Learning class.

This model will take in a character's DnD stats and output a recommended starting class.

## How to run

First, create an empty directory in root called `/data`. This directory will hold all the needed CSV's. Next, download this data set and place it in the `/data` folder: https://www.kaggle.com/datasets/maximebonnin/dnd-characters-test/data

Next, run the python script `create-data.py`. This script converts the dataset in the `/data` folder into data we can use for our model.

Finally, run the python script `decision-tree.py`. This script will create our model and ask for input on `stdin` about your character's stats. Please only enter positive numbers as input.