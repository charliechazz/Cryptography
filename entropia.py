from math import log10

frec_esp = {'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86,
		'E': 13.68, 'F': 0.69, 'G': 1.01, 'H': 0.70, 'I': 6.25, 'J':0.44,
		'K': 0.01, 'L': 4.97, 'M': 3.15, 'N': 6.71, 'O': 8.68,
		'P': 2.51, 'Q': 0.88, 'R': 6.87, 'S': 7.98, 'T': 4.63, 'U':3.93,
		'V': 0.90, 'W': 0.02, 'X': 0.22, 'Y': 0.90, 'Z': 0.52}
		
AEO    = 'EAOSRNIDLCTUMPBGVYQHFZJXWK'

LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Alfabeto

def contar_letras(mensaje): # devuelve un diccionario con letras y frecuencias de cada una de ellas
	num_letras = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
				'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M':0,
				'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
				'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

	for letras in mensaje.upper():
		if letras in LETRAS:
			num_letras[letras] += 1

	return num_letras

def item_indice_primero(x): # voy a retornar por el primer elemento del par ordenado
	return x[0]

def ordenar_frecuencias(mensaje): # devuelve las 26 letras ordenadas de mayor a menor frecuencia
	frec_letras = contar_letras(mensaje)

	frec_a_letras = {} # frecuencia: valores ej {12: ['S'], '56': ['A'], ..

	for letras in LETRAS:
		if frec_letras[letras] not in frec_a_letras:
			frec_a_letras[frec_letras[letras]] = [letras]
		else:
			frec_a_letras[frec_letras[letras]].append(letras)
	
	for freq in frec_a_letras: # recorremos los keys de frec_a_letras los cuales son enteros (int)
		frec_a_letras[freq].sort(key = AEO.find, reverse = True) # por cada elemento del diccionario lo ordenara en funcion a la cadena AEO y lo invertira
		frec_a_letras[freq] = ''.join(frec_a_letras[freq]) # convierte a cadena el vector correspondiente a la key freq

	pares_frec = list(frec_a_letras.items()) # convertimos a pares ordenados las claves y sus valores posteriormente lo convertimos en un vector
	pares_frec.sort(key = item_indice_primero, reverse = True) # vamos a ordenar por el key del vector y lo vamos a invertir
	# (key, value) -> key

	orden_frec = []

	for par in pares_frec:
		orden_frec.append(par[1]) # orden_frec = ['A', 'B', 'C']

	return ''.join(orden_frec) # orden_frec = 'ABC'

def indice_frec_esp(mensaje): # devuelve el numero de coincidencias que tiene el mesaje cuando se compara sus frecuencias con las del español
	orden_frec = ordenar_frecuencias(mensaje)

	indice = 0
	# Halla cuantas letras de las 6 mas comunes hay
	for mas_comun in AEO[:6]:
		if mas_comun in orden_frec[:6]:
			indice += 1
	return indice

def letras_tot(mensaje):
	fk = contar_letras(mensaje).values()
	N = 0 # variable para contar

	for num in fk:
		N += num
	return N, fk # retornaremos un par ordenado (N, fk)

def ic(mensaje): # devuelve el indice de coincidencia

	# el IC para el castellano es aproximadamente: IC = 0.0775

	ind = 0
	N = letras_tot(mensaje)[0]
	fk = letras_tot(mensaje)[1]

	for num in fk:
		ind += num * (num - 1)
	ind = ind / (N * (N - 1))

	return abs(ind) # |ind|

def entropia(mensaje): # entropia
	# La entropia para el castellano es aproximadamente: H = 4.04
	H = 0
	N = letras_tot(mensaje)[0]
	fk = letras_tot(mensaje)[1]
	for num in fk:
			if num != 0:
				H += num/N * (log10(num/N) / log10(2))
	return -H

mensaje = input("Introduce mensaje: ").upper()

print("Indice de frecuencia:", indice_frec_esp(mensaje))
print("Indice de coincidencia:", ic(mensaje))
print("Entropia:", entropia(mensaje))