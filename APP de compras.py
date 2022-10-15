precio1=input("cuanto es el precio 1?: ")
cantidad1=input("cuanta cantidad compras del primero?: ")
precio2=input("cuanto es el precio 2?: ")
cantidad2=input("cuanta cantidad compras del segundo?: ")
precio3=input("cuanto es el precio 3?: ")
cantidad3=input("cuanta cantidad compras del tercero?: ")


resultado1=float(precio1)*float(cantidad1)
resultado2=float(precio2)*float(cantidad2)
resultado3=float(precio3)*float(cantidad3)
resultadototal=resultado1+resultado2+resultado3

print("esto gastaras en el primer bien: "+str(resultado1))
print("esto gastaras en el segundo bien: "+str(resultado2))
print("esto gastaras en el tercer bien: "+str(resultado3))
print("esto gastaras en Total: "+str(resultadototal))
