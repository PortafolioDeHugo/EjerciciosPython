def love(name):
    print("I love "+name)

love("MANAOS")

def persona_1(nombre):
    print(nombre+": Hola como puedo ayudarte?")


def persona_2(comida,bebida,postre,nombre):
    print("?: Me gustaria comprar algo")
    nombre=input("Cual es tu nombre? ")
    comida=input("Que te gustaria comer? ")
    bebida=input("Que te gustaria beber? ")
    postre=input("Que te gustaria de postre? ")
    print(nombre+": A mi me gustaria "+comida+" con una "+bebida+" y de postre "+postre )

def persona_1_2(nombre):
    print(nombre+ ": Aqui tiene, Muchas Gracias por venir, Tenga Buen Dia")

persona_1("Cajera")
persona_2("comida","bebida","postre","nombre")
persona_1_2("Cajera")