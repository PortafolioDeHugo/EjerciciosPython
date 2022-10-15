I_want_to_eat = False
I_want_to_drink = True


if not I_want_to_eat :
    print("let's go to the restaurant")
elif I_want_to_drink :
    print("let's have a drink")
else:
    print("I'm good")



var1=5
var2=6
var3=2

if var1>var2:
    print("yes")
else:print("no")



var1="Rojo"
var2="Verde"
var3="Azul"
var4="Amarillo"

if var1==var2:
    print("Yes")
else: print("no")




Nombre_usuario1 = input("Cual es tu nombre ?: ")
Dinero_usuario1 = input("Cuanto dinero Tenes ?: ")

Nombre_usuario2 = input("Cual es tu nombre ?: ")
Dinero_usuario2 = input("Cuanto dinero Tenes ?: ")

Nombre_usuario3 = input("Cual es tu nombre ?: ")
Dinero_usuario3 = input("Cuanto dinero Tenes ?: ")

if float(Dinero_usuario1) > float(Dinero_usuario2) and float(Dinero_usuario1) > float(Dinero_usuario3):
    print(Nombre_usuario1+" Es el que mayor plata posee")

elif float(Dinero_usuario2) > float(Dinero_usuario1) and float(Dinero_usuario2) > float(Dinero_usuario3):
    print(Nombre_usuario2 + " Es el que mayor plata posee")

elif float(Dinero_usuario3) > float(Dinero_usuario1) and float(Dinero_usuario3) > float(Dinero_usuario2):
    print(Nombre_usuario3 + " Es el que mayor plata posee")

else: print("Son todos Igualmente de  Pobres")