abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cadena = "KYZUE VKTYGTJU IUT WAO KT OX KR JOG JK SG GTG, VXUHGHR KSKTZK O TBOZK G GRKPGTJX G U PUYK... TUYK"
key = 32

cadena = cadena.upper() # HOLA

salida = ""

for caracter in cadena:
	

	if caracter in abecedario:
		posicion = abecedario.index(caracter)
		salida += abecedario[(posicion - key) % 26]
	else:
		salida += caracter
	# esta linea es la misma que
	# salida = salida + abecedario[(posicion + key) % 26]
print(salida)