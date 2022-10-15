variable_1="Manzana"
List_1=["manzanas","bananas","Ananas","Limones"]
List_1[3]="Palta"
List_1[2]="Tomates"

Comidas=["hamburguesa","pizza","jugo","papas fritas","Sushi"]
precios=[5.64,3.94,7.29,4.95,3.28]

Comidas.insert(2,"fideos")
precios.insert(2,5.00)

Comidas.extend(precios)  #son iguales en su funcionamiento
random=Comidas.copy()+precios.copy()   #son iguales en su funcionamiento


print(random)

 