cantidad = int(input("Cantidad: "))

numeros = []

for i in range(cantidad):
    numero = int(input())
    numeros.append(numero)

buscado = int(input("Número a buscar: "))

posicion = -1

for i in range(len(numeros)):
    if numeros[i] == buscado:
        posicion = i
        break

if posicion != -1:
    print("El", buscado, "está en la posición", posicion)
else:
    print("El", buscado, "no está en la lista")