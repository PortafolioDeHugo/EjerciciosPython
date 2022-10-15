def preguntas():

    rules = input("Responde todas las preguntas, con si o no , entendido? : ")
    if rules != "si":
        return print("Vuelve a  intentar")
    else: print("Siguiente pregunta")
    pregunta1 = input("usted tiene hanbre? : ")
    if pregunta1 != "si":
        return print("vayamos a caminar")
    else:print("Siguiente Pregunta")
    pregunta2 = input("Quiere ir a algun Restaurant? : ")
    if pregunta2!="si":
        return print("Comamos en mi casa")
    else:print("Siguiente Pregunta")
    pregunta3 = input("Te gustaria Comer una pizza? :")
    if pregunta3!="si":
        return print("Entonces vayamos a comer una Hamburguesa")
    else:print("ok vayamos a comer una pizza")

preguntas()