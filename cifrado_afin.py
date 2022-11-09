alfabeto = """ !¡"#$%&'()*+,-./0123456789:;<=>¿?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{|}~"""

def mcd(a,b):
    while a != 0:
        a = b % a
        b = a
    return b

def invMod(a,m):
    if mcd(a,m) == 1:
        for x in range(1,m):
            if ((a % m) * ( x % m )) % m == 1:
                return x
    return -1


def cifrar_mensaje(texto,clave_A, clave_B):
    critpograma = ''

    for caracter in texto:
        if caracter in alfabeto:
            indice = alfabeto.find(caracter)
            critpograma += alfabeto[(indice * clave_A + clave_B) % len(alfabeto)]
        else: 
            critpograma += caracter
    return critpograma

mensaje = "Hola que tal como estas?. Mañana Asistiras a clases"

clave_A = 23
clave_B = 54

if clave_A < len(alfabeto) and clave_B < len(alfabeto) and mcd(clave_A, len(alfabeto)) != 1:
    print(cifrar_mensaje(mensaje, clave_A, clave_B))
else:
    print(cifrar_mensaje(mensaje,clave_A, clave_B))