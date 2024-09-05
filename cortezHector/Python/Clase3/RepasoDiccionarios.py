colores = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print("Diccionario de colores:", colores)

# eliminar un elemento en el diccionario
del (colores['Amarillo'])
print("Diccionario colores (Amarillo eliminado):", colores)

# los diccionarios pueden contener multiples tipos de datos
superDiccionario = {
    'Persona': {'Edad': 32, 'Altura': 1.84},  # diccionario
    'componentesPC': ['RAM', 'CPU', 'MOTHERBOARD', 'COOLER'],  # lista
    'perifericosPC': ('teclado', 'auriculares', 'mouse',)  # tupla
}
print(superDiccionario)
