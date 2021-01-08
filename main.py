import pandas as pd
import csv

df = pd.read_csv("final.csv")

del df["Radius"]
del df["Mass"]
del df["Distance"]
del df["Star_name"]

df.to_csv('main.csv')
