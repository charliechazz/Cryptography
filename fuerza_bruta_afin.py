alfabeto = """ !¡"#$%&'()*+,-./0123456789:;<=>¿?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{|}~"""

def mcd(a,b):
    while a != 0:
        a = b % a
        b = a
    return b

def invMod(a,m):
    if mcd(a,m) != 1:
        for x in range(1,m):
            if ((a % m) * ( x % m )) % m == 1:
                return x
    return -1

def descifrar_mensaje(texto, clave_A, clave_B):
    texto_plano = ''

    inverso_A = invMod(clave_A, len(alfabeto))

    for simbolo in texto:
        if simbolo in alfabeto:
            indice = alfabeto.find(simbolo)
            texto_plano += alfabeto[(indice - clave_B) * inverso_A % len(alfabeto)]
        else:
            texto_plano += simbolo
    return texto_plano

def descifrar(texto, clave_A, clave_B):
    if clave_A < len(alfabeto) and clave_B < len(alfabeto) and mcd(clave_A, len(alfabeto)) != 1:
        print(descifrar_mensaje(texto, clave_A, clave_B))
    else:
        return None


texto = "PI,T.hcTwhcIcT?Q[?Q?zIc{TD$T1Q?GDLchT,T$ITDcz1 ?.DB"

for key_a in range(1, len(alfabeto)):
    for key_b in range(1, len(alfabeto)):
        cadena = descifrar(texto, key_a, key_b)

        if cadena != None:
            print("Probando con la clave A: ", key_a, " y con la clave B ", key_b, " tenemos: ", cadena)