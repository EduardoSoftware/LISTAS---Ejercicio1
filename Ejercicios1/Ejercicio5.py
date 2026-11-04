n = int(input("¿Cuántas letras? "))

letras = []

for i in range(n):
    letra = input("Letra: ")
    letras.append(letra)

conteo_a = 0
conteo_e = 0
conteo_i = 0
conteo_o = 0
conteo_u = 0

for letra in letras:
    if letra == 'a':
        conteo_a = conteo_a + 1
    elif letra == 'e':
        conteo_e = conteo_e + 1
    elif letra == 'i':
        conteo_i = conteo_i + 1
    elif letra == 'o':
        conteo_o = conteo_o + 1
    elif letra == 'u':
        conteo_u = conteo_u + 1

print("a:", conteo_a)
print("e:", conteo_e)
print("i:", conteo_i)
print("o:", conteo_o)
print("u:", conteo_u)