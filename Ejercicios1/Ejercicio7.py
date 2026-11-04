cantidad = int(input("Cantidad de temperaturas: "))

temperaturas = []
suma = 0

for i in range(cantidad):
    temp = float(input())
    temperaturas.append(temp)
    suma = suma + temp

if cantidad > 0:
    media = suma / cantidad
else:
    media = 0

mayores = []

for temp in temperaturas:
    if temp >= media:
        mayores.append(temp)

print("Temperatura media:", media)
print("Temperaturas >= media:", mayores)
print("Total:", len(mayores))