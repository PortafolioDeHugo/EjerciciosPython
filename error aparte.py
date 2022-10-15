import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

plt.scatter(data.tiempo, data.aprobado)

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points))
        x = points.iloc[i].tiempo
        y = points.iloc[i].aprobado
        total_error += (y -(m * x + b)) ** 2
    total_error / float(len(points))
