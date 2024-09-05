# Ejercicio con tuplas (Selección Argentina):
# ingresar elementos al diccionario llamado seleccionArgentina,
# los elementos a ingresar deben ser como mínimo 4,
# estos elementos son los jugadores con su número de camiseta,
# nombre, apellido, edad, altura, precio y posición de juego.
seleccionArgentina = {
    10: {'nombre': 'lionel messi', 'edad': 35, 'altura': 1.70, 'precio': '50 millones', 'posicion': 'extremo derecho'},
    11: {'nombre': 'angel di maria', 'edad': 34, 'altura': 1.80, 'precio': '12 millones',
         'posicion': 'extremo derecho'},
    24: {'nombre': 'paulo dybala', 'edad': 28, 'altura': 1.77, 'precio': '35 millones', 'posicion': 'media punta'},
    19: {'nombre': 'nicolas otamendi', 'edad': 34, 'altura': 1.83, 'precio': '3.5 millones',
         'posicion': 'defensa central'}
}

# muestra solo las llaves
for key in seleccionArgentina.keys():
    print(key)

print()

# muestra solo las valores
for value in seleccionArgentina.values():
    print(value)

print()

# muestra las llaves con los valores
for item in seleccionArgentina.items():
    print(item)
