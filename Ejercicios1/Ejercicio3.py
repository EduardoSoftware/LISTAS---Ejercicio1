"""
• Mostrar el nombre completo (nombre y apellido).
• Mostrar el año de nacimiento.
• Mostrar cuántos elementos tiene la tupla del registro.
• Mostrar cuál es el cuarto elemento de la tupla.
"""

nombre = ["Eduardo", "Rincon"]
nacimiento = (30, 7, 2003)

nombre.extend(nacimiento)

print(nombre)


print(f"El nombre del camper es: {(nombre[0:2])}, Su anio de nacimiento es: {(nombre[-1])}, La tupla tiene {len(nombre)} elementos, La cuarta posicion de la tupla es: {(nombre[4])} ")



