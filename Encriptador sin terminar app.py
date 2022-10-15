
def criptado (oracion):           #nombre de la funcion "criptado"
    Encriptado=""
    for elementos in oracion:     #buscar en cada elemnto de la oracion
        if elementos in "Aa":     #aca buscara si aparece una A o una a minuscula
            Encriptado=Encriptado+"1"
        elif  elementos in "Bb":
            Encriptado = Encriptado + "2"
        elif elementos in "Cc":
            Encriptado = Encriptado + "3"
        elif elementos in "Dd":
            Encriptado = Encriptado + "4"
        elif elementos in "Ee":
            Encriptado = Encriptado + "5"
            .
            .
            .
        elif elementos in "Yy":
            Encriptado = Encriptado + "}"
        elif elementos in "Zz":
            Encriptado = Encriptado + "{"
        else:
            Encriptado = Encriptado+elementos

    return Encriptado

print(criptado(input(" Que te gustaria Encriptar: ")))