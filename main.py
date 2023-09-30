import csv

import pandas as pd

import plotly_express as px

df1 = pd.read_csv("scraped-data.csv")
print(df1["mass"])

data1 = []

df1["mass"] = df1["mass"]*0.102763
df1["radius"] = df1["radius"]*0.000954588

print(df1["mass"])

print(df1.describe())
print(df1.info())
print(df1.dtypes)

df1.to_csv("final_data.csv")

df1["gravity"] = 6.6*10**-11 * df1["mass"]/df1["radius"]**2
print(df1)
df1.to_csv("final_data_with_gravity.csv")

solar_chart_mass_radius_graph = px.scatter(x=df1["mass"],y=df1["radius"])
solar_chart_mass_radius_graph.show()

solar_chart_mass_radius_list = []
solar_chart_mass_radius_list.append(df1["mass"])
solar_chart_mass_radius_list.append(df1["radius"])