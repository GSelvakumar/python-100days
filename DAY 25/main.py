# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas 

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

# #Get data in row
# print(data[data.day == "Monday"])

# #To get the maximum temperature from the temp column
# print(data[data.temp == data.temp.max()])

#To get monday temperature in Farh.
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#create a dataframe from scratch

data_dict = {
    "students": ["Amy", "Anwar"],
    "scores": [45, 54]
}

data = pandas.Dataframe(data_dict)
data.to_csv("new_data.csv")
