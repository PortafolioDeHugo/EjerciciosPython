
Contrasena="pass123"
respuesta=""
numbero_de_intentos=0                                                                      #para cualquier APP debes crear sus variables previamente
numbero_maximo_de_intentos=8
Intento_maximo="No se alcanzo el maximo intentos "

while respuesta!=Contrasena and Intento_maximo!="se alcanzo el maximo intentos":           #recordar poner ":" al final de estas oraciones
      if numbero_de_intentos<numbero_maximo_de_intentos:
          respuesta=input("Cual es la contrasena?: ")           #con el condicionante anterior, buscar una contrasena
          numbero_de_intentos=numbero_de_intentos+1             
      else:
          Intento_maximo = "se alcanzo el maximo intentos"

if Intento_maximo=="se alcanzo el maximo intentos" :
    print("Se alcanzo el maximo intentos Cuenta Bloqueada")

else:print("Acceso Concedido")