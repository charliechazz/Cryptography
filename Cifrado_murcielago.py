print("Cifrado MURCIÉLAGO")
print("1) Cifrar")
opcion=int(input("Introduce la opción: "))

cantidad = int(input("Cuántas palabras?: "))

for i in range(cantidad):
    print("Escriba su palabra #",i + 1,": ")
    texto=input().lower()
    codigo=['m','u','r','c','i','e','l','a','g','o']
    salida=''
    for i in range(len(texto)):
        if texto[i] in codigo:
            salida += str(codigo.index(texto[i]))
        else:
            salida+=texto[i]

if opcion==1:
    for i in range(len(texto)):
        if texto[i] in codigo:
            salida += str(codigo.index(texto[i]))
        else:
            salida+=texto[i]


print(salida.upper())