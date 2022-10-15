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

def gradient_descent(m_now, b_now, points, L):        #derivadas parciales con error incluido
                                                      #de las 2 variables de la base de datos
    m_gradient = 0
    b_gradient = 0

    n = len(points)                                #define 3 variables dentro de la funcion

    for i in range(n):
        x = points.iloc[i].tiempo                 #utiliza los datos de DATA.csv para hacerlos variar y cambiar
        y = points.iloc[i].aprobado               #a base de las derivadas parciales del error en un loop for
                                                                            #una vez creado el loop, seguira procesandolo
        m_gradient += -(2/n)  * x *   (y - (m_now * x + b_now))             #por cada i en el rango N a definir
        b_gradient += -(2/n) *   (y - (m_now * x + b_now))                  #en este caso los puntos en la DATA

    m = m_now - m_gradient * L                                      #define m y b como calculos a obtener luego del loop
    b = b_now - b_gradient * L
    return m, b

m = 0
b = 0                                                #les da valores base a m, b , L(lerning rate) y periodos para
L = 0.0001                                           #el loop for siguiente, que utilizara tanto estas variables como
epochs = 100                                         #la funcion o aplicacion anterior que busca en los puntos las derivadas



for i in range(epochs):                                             #a base del rango de epochs busca crear iteracciones
    if i % 50 == 0:                                                 #para que el programa aprenda
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, data, L)                 #utiliza el programa anterior y sus definiciones

print(m, b)

plt.scatter(data.tiempo, data.aprobado, color="black")
plt.plot(list(range(20, 50)), [m * x + b for x in range(20, 50)], color="green")
plt.show()
