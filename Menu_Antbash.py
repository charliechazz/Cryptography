print("Codificador/Decodificar AtBash")
print("1) Codificar")
print("2) Decodificar")

opcion = int(input("Introduce: "))

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alrevez =    "ZYXWVUTSRQOINMLKJIHGFEDCBA"

cadena = input("Introduce cadena: ")

cadena = cadena.upper()

salida = ""

if opcion == 1:
	for caracter in cadena:
		posicion = abecedario.index(caracter)
		salida = salida + alrevez[posicion]
		
if opcion == 2:
	for caracter in cadena:
		posicion = alrevez.index(caracter)
		salida = salida + abecedario[posicion]

print(salida)