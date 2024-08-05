import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240804.csv")

gray_squi = len(data[data["Primary Fur Color"] == "Gray"])

black_squi = len(data[data["Primary Fur Color"] == "Black"])

red_squi = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "fur color" : ["gray", "red", "black"],
    "count": [gray_squi, red_squi, black_squi]
}

df = pandas.DataFrame(data_dict)
df.to_csv("New dataframe")