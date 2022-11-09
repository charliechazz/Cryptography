abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cadena = "MTQF VZJ YFQ HTRT JXYFX YJ AJT RFÑFSF JS HQFXJX"

cadena = cadena.upper() # HOLA

for key in range(0, 26): # range 0, 1, 2, 3, 4, ..., 25
# range(x, y): vas a recorrer desde x hasta y - 1
	salida = ""

	for caracter in cadena:
		if caracter in abecedario:
			posicion = abecedario.index(caracter)
			salida += abecedario[(posicion + key) % 26]
		else:
			salida += caracter
	print("Probando para la clave", key, ": ", salida)