import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")

figure = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = False)
figure.show()