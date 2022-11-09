ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
GIRO = len(ALFABETO) // 2 - 1 # 12
NUMERO = 5 # Numero de alfabetos

#global entrada
#global alfabeto

alfabeto = [''] * NUMERO # contendra los cinco alfabetos de la tabla reciproca

entrada = [''] * NUMERO # esta formada por cinco cabeceras, las filas

def main():
	clave = input("Clave para los alfabetos: ").upper()
	clave = quitar_duplicados(clave)

	global entrada
	global alfabeto

	entrada, alfabeto = generar_alfabetos(clave)

	op = input("¿Deseas cifrar(c) o decifrar(d)?: ").upper()

	if op == "C":
		mensaje = input("Introduce el mensaje: ").upper()
		password = input("Clave: ").upper()
		criptograma = cifrarMensaje(password, mensaje)
		print("El criptograma es: ", criptograma)
	if op == "D":
		criptograma = input("Introduce el criptograma: ").upper()
		password = input("Clave: ").upper()
		texto = descifrarMensaje(password, criptograma).lower()
		print("El texto plano es: ", texto)

def quitar_duplicados(clave): # Algoritmo para eliminar elementos duplicados en un vector
	nueva_clave = ''

	# otra forma de hacer esto es con un conjunto NO ordenado

	# Por ejemplo: "abaa" -> "ab"

	global entrada
	global alfabeto

	for letra in clave:
		if letra not in nueva_clave: # verifica que la letra no este en la nueva_clave
			nueva_clave += letra
	clave = nueva_clave

	return clave
def generar_alfabetos(clave):
	# Defninimos como se coloca la clave en los alfabetos

	clave1_1 = str()
	clave1_2 = str()

	longitud = len(clave) # la longitud de la clave

	if longitud % 2 == 0: # Verificar si la clave es de longitud par
		for j in range(0, longitud // 2):
			clave1_1 += clave[j]
		for j in range(longitud // 2, longitud):
			clave1_2 += clave[j]
	else:
		limite = (longitud + 1) // 2
		for j in range(0, limite):
			clave1_1 += clave[j]
		for j in range(limite, longitud):
			clave1_2 += clave[j]

	# generamos el primer alfabeto

	alf1_1 = clave1_1
	alf1_2 = clave1_2
	s_alf = [''] * 2 * NUMERO

	# Recorremos el ALFABETO general y vamos agregando a alf1_1 y alf1_2 cada letra correspondiente

	for i in ALFABETO:
		if i not in clave and len(alf1_1) <= GIRO:
			alf1_1 += i

	for j in ALFABETO:
		if j not in clave and len(alf1_2) <= GIRO and j not in alf1_1:
			alf1_2 += j

	s_alf[0] = alf1_1
	s_alf[1] = alf1_2

	alfabeto[0] = s_alf[0] + s_alf[1] # hacemos una concatenacion con las dos particiones s_alf[0] = alf1_1 y s_alf[1] = alf1_2

	# Entradas de los alfabetos

	for k in range(0, NUMERO):
		for i in range(k, len(alfabeto[0]), NUMERO):
			entrada[k] += alfabeto[0][i]

	# Para el resto de los alfabetos

	for k in range(2, 2 * NUMERO):
		if k % 2 == 0: # Alfabeto Par
			s_alf[k] = s_alf[0]
		else: # Alfabeto Impar
			for i in range(0, len(s_alf[0])):
				pos = (i + GIRO) % len(s_alf[0])
				s_alf[k] += s_alf[k - 2][pos]

			alfabeto[(k - 1) // 2] = s_alf[0] + s_alf[k]

	mostrar_tabla(entrada, s_alf)

	return (entrada, alfabeto)


def mostrar_tabla(entrada, s_alf):
	print("Tabla Reciproca: ")
	for i in range(0, NUMERO):
		print(entrada[i], end = '')
		if len(entrada[i]) - len(entrada[0]) == 0:
			print(" ", s_alf[0].lower())
		else:
			print(" " * 2, s_alf[0].lower())

		espacios = len(entrada[0]) * 2
		print(' ' * espacios, end = '')
		print(s_alf[2*i + 1].lower())

def busqueda(clave): # devuelve el numero de alfabeto
	for i in range(0, len(entrada)):
		if clave[0] in entrada[i]:
			return i
	return 0

def cifrarMensaje(clave, mensaje):
	return cifrar_descifrar(clave, mensaje, 'cifrar').upper()
def descifrarMensaje(clave, mensaje):
	return cifrar_descifrar(clave, mensaje, 'descifrar').lower()

def cifrar_descifrar(clave, mensaje, modo)	:
	palabras = mensaje.split() # Separamos el texto por espacios es decir por ejemplo: "Hola que tal" -> ['Hola', 'que', 'tal']
	salida = ''

	if modo == "cifrar" or modo == "descifrar":
		for i in range(0, len(palabras)):
			n = busqueda(clave[i % len(clave)])

			for j in range(0, len(palabras[i])):
				indice = (n + j) % len(entrada)

				pos = alfabeto[indice].find(palabras[i][j])

				if pos == -1: # no encuentra el simbolo
					salida += palabras[i][j]
				else:
					pos = (pos + len(ALFABETO) // 2) % len(ALFABETO)
					salida += alfabeto[indice][pos]

			salida += ' '

	return salida

if __name__ == '__main__':
	main()