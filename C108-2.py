import plotly.figure_factory as ff 
import pandas as pd 
import csv

df=pd.read_csv("D:/C-108/data.csv")

#fig=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)
fig=ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
fig.show()