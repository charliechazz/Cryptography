mensaje = "HivcpsooaiiopnldmfroaeortsEhsariloedacdyloni"

for clave in range(0,1000):
    clave = 1 # para hacer fuerza bruta esta clave debe iterar desde 0 hasta la longitud del mensaje codificado

num_col = (len(mensaje) // clave) + 1

num_filas = clave

celdas_vacias = (num_col * num_filas) - len(mensaje)

texto_plano = [''] * num_col

col = 0
fila = 0

for caracter in mensaje:
	texto_plano[col] += caracter
	col += 1

	if col == num_col or (col == num_col - 1 and fila >= num_filas - celdas_vacias):
		col = 0
		fila += 1

salida = str()

for elemento in texto_plano:
	salida += elemento
print(salida)