"""
• Mostrar las tres primeras canciones.
• Mostrar las dos últimas canciones.
• Mostrar las canciones que ocupan las posiciones tercera, cuarta y quinta.
"""

canciones = ('Colombia tierra querida','La pollera colorá', 'Mi Buenos Aires querido', 'El Pescador', 'Fruta fresca','La bicicleta', 'Antología')

print(f"""
Apertura: {canciones[0:3]}
Cierre: {canciones[-2:]}
Momento de bailar: {canciones[2:5]}
""")