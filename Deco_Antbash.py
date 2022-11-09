abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alrevez =    "ZYXWVUTSRQOINMLKJIHGFEDCBA"

cadena = "Sliz"

cadena = cadena.upper()

salida = ""

for caracter in cadena:
	posicion = alrevez.index(caracter)
	salida = salida + abecedario[posicion]

print(salida)
