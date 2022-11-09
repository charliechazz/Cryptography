abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#cadena = "El dia de hoy pasamos el cifrado atbash y cesar"
cadena = "ESTOY PENSANDO CON QUIEN IR EL DIA DE MA ANA, PROBABLEMENTE INVITE A ALEJANDRA O JOSE... NOSE"
#key = 66
key = 32

cadena = cadena.upper() # HOLA

salida = ""

for caracter in cadena:
	if caracter in abecedario:
		posicion = abecedario.index(caracter)
		salida += abecedario[(posicion + key) % 26]
	else:
		salida += caracter
	# esta linea es la misma que
	# salida = salida + abecedario[(posicion + key) % 26]
print(salida)