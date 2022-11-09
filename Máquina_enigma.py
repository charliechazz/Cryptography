# Maquina enigma M3

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Grundstellung
inicio = ('O', 'Y', 'B') # posicion inicial de los rotores-

# Walzenlage
rotores = (4, 2, 3) # El tipo y el orden de los mismos

# Umkehrwalze
reflector = 'B' # Tipo de reflector (UKW)

# Ringstellung
posicion_interna = ('Z', 'N', 'K') # posicion interna

# Steckerverbindungen
clavijero = [('Z','N'), ('Y','O'), ('Q','B'), ('E', 'R'), ('D','K'), ('X','U'), ('G','P'), ('T','V'), ('S','J'), ('L','M')]

cableado_rotor = ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', # 1
	'AJDKSIRUXBLHWTMCQGZNPYFVOE',				# 2
	'BDFHJLCPRTXVZNYEIWGAKMUSQO',				# 3
	'ESOVPZJAYQUIRHXLNFTGKDCMWB',				# 4
	'VZBRGITYUPSDNHLXAWMJQOFECK',				# 5
	'JPGVOUMFYQBENHZRDKASXLICTW',				# 6
	'NZJHGRCXMYSWBOUFAIVLPEKQDT',				# 7
	'FKQHTLXOCBJSPDZRAMEWNIUYGV')				# 8

cableado_reflector = ('EJMZALYXVBWFCRQUONTSPIKHGD',
					'YRUHQSLDPXNGOKMIEBFZCWVJAT',
					'FVPJIAOYEDRZXWGCTKUQSBNMHL')
def main():
	print("Maquina Enigma M3")
	print("1) Cifrar")
	print("2) Descifrar")
	print("3) Salir")

	op = int(input("Opcion (1/2): "))

	if op == 1:
		mensaje = input("Introduce mensaje: ")
		texto = cifrar(mensaje)
		print(texto)
	elif op == 2:
		mensaje = input("Introduce mensaje: ")
		texto = descifrar(mensaje)
		print(texto)
	else:
		print("Fin")

def vuelta(cableado):
	# Sigue por rotor el recorrido de vuelta dela señal desde el reflector

	salida = str()

	for i in alfabeto:
		salida += alfabeto[cableado.find(i)]
	return salida

def cableado_inverso():
	inverso = list()

	for i in range(0, len(cableado_rotor)):
		inverso.append(vuelta(cableado_rotor[i]))
	inverso = tuple(inverso)

	return inverso

inverso = cableado_inverso()

inicio = list(inicio) # lo volvemos a vector la tupla

muesca = (('Q',), ('E',), ('V',), ('J',), ('Z',), ('Z','M'), ('Z','M'), ('Z','M'))

rotores = (3, 1, 2)

def numero(car):
	# Esta funcion devuelve el numero correspondiente a cada caracter

	car = car.upper()

	arr = {'A':0,'B':1,'C':2, 'D':3,'E':4, 'F':5, 'G':6,
			'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12,
			'N':13, 'O':14, 'P':15, 'Q':16, 'R':17,'S':18,
			'T':19, 'U':20, 'V':21, 'W':22,'X':23,'Y':24, 'Z':25}

	return arr[car]

reflector = numero(reflector) # B -> 1

def rotor(letra, veces, cableado_rotor):
	# Esto nos permite seguir el recorrido de la corriente electrica tanto de camino de ida como de vuelta

	letra = sustituye(letra, cableado_rotor, veces)

	return sustituye(letra, alfabeto, -veces)

def refleja(letra):
	# esta encargada de simular el paso de la señal del reflector
	return sustituye(letra, cableado_reflector[reflector], 0)

def sustituye(letra, ALFABETO, veces):
	# sustituye una letra de acuerdo a la clave
	indice = (numero(letra) + veces) % 26

	return ALFABETO[indice]

def aplicar_clavijero(letra):
	# simula el comportamiento del intercambio de los pares de letras

	for elemento in clavijero:
		if letra == elemento[0]:
			return elemento[1]
		if letra == elemento[1]:
			return elemento[0]
	return letra

def rotor_avanza():
	# Simula el avance de los rotores
	if inicio[1] in muesca[rotores[1]]:
		inicio[0] = sustituye(inicio[0], alfabeto, 1)
		inicio[1] = sustituye(inicio[1], alfabeto, 1)

	if inicio[2] in muesca[rotores[2]]:
		inicio[1] = sustituye(inicio[1], alfabeto, 1)
	inicio[2] = sustituye(inicio[2], alfabeto, 1)

def cifrar_caracter(letra):
	rotor_avanza()
	letra = aplicar_clavijero(letra)

	# Camino de ida de la señal

	for i in range(2, -1, -1): # 2, 1, 0
		veces = ord(inicio[i]) - ord(posicion_interna[i])

		letra = rotor(letra, veces, cableado_rotor[rotores[i]])

	# Entrada y salida por el reflector

	letra = refleja(letra)

	# Camino de vuelta

	for i in range(0, 3): # 0, 1, 2
		veces = ord(inicio[i]) - ord(posicion_interna[i])
		letra = rotor(letra, veces, inverso[rotores[i]])

	# Salida del clavijero

	letra = aplicar_clavijero(letra)

	return letra

def descifrar(texto):
	# cifrar = descifrar
	return cifrar(texto)

def cifrar(texto):
	texto = texto.upper()

	salida = str()

	for c in texto:
		if c.isalpha() == True and c.upper() != 'Ñ': # alpha verifica si pertence al abecdario español pero debemos evitar la Ñ ya que la Ñ es propia del español
			salida += cifrar_caracter(c)
		else:
			salida += c
	return salida

main()