import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
#para ver la base de datos Print(data)

plt.scatter(data.tiempo, data.aprobado)
#para verla en un grafico con la segunda libreria instalada
#plt.show()

def loss_function(m, b, points):    #esto es el error de la formula
    total_error = 0                 #de manera manual ,
    for i in range(len(points)):    #en este ejerecicio no se utilizara
        x = points.iloc[i].tiempo
        y = points.iloc[i].aprobado
        total_error += (y - (m * x + b)) ** 2
    total_error / float(len(points))

def gradient_descent(m_now, b_now, points, L):     #derivadas parciales con error incluido
                                                  #de las 2 variables de la base de datos
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].tiempo
        y = points.iloc[i].aprobado

        m_gradient += -(2/n)  * x *   (y - (m_now * x + b_now))
        b_gradient += -(2/n) *   (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

m = 0
b = 0
L = 0.0001
epochs = 1000
