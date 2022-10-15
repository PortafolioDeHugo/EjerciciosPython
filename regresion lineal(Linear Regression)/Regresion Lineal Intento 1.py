#Regresion Lineal 

#Insertar DATA

x = [10, 20, 30, 50, 65, 70, 90, 260, 210, 320 ]
y = [100, 200, 250, 300, 324, 405, 478, 521, 700,750]

 
#obtenemos primero los promedios 
PromedioX = sum(x)/len(x)
PromedioY = sum(y)/len(y)

#Luego obtenemos X-Xraya e Y-Yraya
def Xi_X():
    rest = []
    for n in x:
        X2 = n-PromedioX
        rest.append(X2)
    return rest    

A = Xi_X()        

def Yi_Y():
    rest = []
    for n in y:
        Y2 = n-PromedioY
        rest.append(Y2)
    return rest    

B = Yi_Y()


A_B  = [i1 * i2 for i1, i2 in zip(A, B)]
 
power_value = 2
AA = list()
for item in A:
    AA.append(pow(item, power_value))

B1 = sum(A_B)/sum(AA)

B0 = PromedioY-PromedioX*B1

Regresion_Lineal_Puntos = list()
for n2 in x:
        RL = round((B1*n2)+ B0)
        Regresion_Lineal_Puntos.append(RL) 
    
print(Regresion_Lineal_Puntos)

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.plot(x,Regresion_Lineal_Puntos)
plt.show()



