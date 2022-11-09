mensaje = "USOS WMVJP YZOZ BPEFZYPKP"

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"

clave    = "ZDKOPWRGTNIMFYSBLECUVXQAJÑH"

clave_aux = list(clave) # convierto en vector la clave

clave_aux.sort() # ordenamos el vector 

clave_aux = ''.join(clave_aux) # convirtiendolo a cadena

if alfabeto == clave_aux: # comparamos que el alfabeto sea igual a la clave ordenada
	criptograma = str()

	for caracter in mensaje:
		if caracter in alfabeto:
			indice = clave.find(caracter)
			criptograma += alfabeto[indice]
		else:
			criptograma += caracter
	print(criptograma)
else:
	print("La clave no es la correcta")