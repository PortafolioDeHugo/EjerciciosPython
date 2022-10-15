
persona1=input("como se llama?")
persona2=input("como se llama?")
persona3=input("como se llama?")

precioporpizza=input("cual es el costo de la pizza?")
porcionesporpizza=input("cuantas porciones tiene la pizza ?")

consumo1=input(persona1+" cuantas ,en porcentaje,comio?")
consumo2=input(persona2+" cuantas ,en porcentaje,comio?")
consumo3=input(persona3+" cuantas ,en porcentaje,comio?")

totaldepizza1=float(consumo1)*float(porcionesporpizza)
totaldepizza2=float(consumo2)*float(porcionesporpizza)
totaldepizza3=float(consumo3)*float(porcionesporpizza)

cuantopago1=float(consumo1)*float(precioporpizza)
cuantopago2=float(consumo2)*float(precioporpizza)
cuantopago3=float(consumo3)*float(precioporpizza)

print(persona1+" comio"+str(totaldepizza1)+"  porciones y pago : $"+str(cuantopago1))
print("           ")
print(persona2+" comio"+str(totaldepizza2)+"  porciones y pago : $"+str(cuantopago2))
print("           ")
print(persona3+" comio"+str(totaldepizza3)+"  porciones y pago : $"+str(cuantopago3))
