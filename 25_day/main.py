import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
temp_list = data["temp"].to_list()

print(data["list"].mean())