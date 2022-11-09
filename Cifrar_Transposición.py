mensaje = "Josetieneunautodecolorrojo"
clave = 5

sin_espacios = str() # "" -> "Holcomoestas"

for caracter in mensaje:
	if caracter != " ": # caracter es diferente de espacio
		sin_espacios += caracter

mensaje = sin_espacios

criptograma = [''] * clave

for columna in range(0, clave):
	pos = columna

	while pos < len(mensaje):
		criptograma[columna] += mensaje[pos]
		pos += clave

salida = str() # ""

for elemento in criptograma:
	salida += elemento
print(salida)
