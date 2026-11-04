"""
Un profesor de matemáticas quiere un programa para que sus estudiantes practiquen la clasificación
de números.
El estudiante digita números enteros, uno por uno, y el programa los va guardando en
una lista.
Cuando el estudiante escribe 99999, deja de pedir números (el 99999 no se guarda).
Al final, el programa debe decir cuáles números son pares y cuántos son, y cuáles son impares y
cuántos son.
"""

pares = []
impares = []

while True:
    numero = int(input("Digite un número: "))
    
    if numero == 99999:
        break
        
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Pares:", pares, "(total", len(pares), ")")
print("Impares:", impares, "(total", len(impares), ")")




