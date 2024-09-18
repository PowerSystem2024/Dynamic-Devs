#Repaso de set o conjunto
#para definir un conjunto
conjunto2 = set() #para inicializar un conjunto vacio tiene que ser con set
conjunto1 = {'Hola'} #para inicializar un conjunto con {} tiene que tener al menos 1 elemento
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('bye')
print(conjunto1)
print(3 not in conjunto1) # preguntamos si el numero 3 no esta en el conjunto1

#como hacer la igualdad de dos conjuntos
print(conjunto1 ==conjunto2) #nos devuelve un boleeano


#operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #que elemento tienen en comun
print(conjunto3)

conjunto3 =conjunto1 - conjunto2 #asigna que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3=conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) #preguntamos si un conjuntos es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))

print(conjunto3.issuperset(conjunto1)) #preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

#como saber si ambos conjuntos con disconexos, estos es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))

#convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #esto hace que el conjunto sea totalmente imutable
#no se puede agregar, modificar ni eliminar elementos del conjunto

# REPASO DICCIONARIOS
diccionarioNuevo = {'Azul': 'Blue','Rojo':'Red', 'Verde':'Green','Amarillo':'Yellow'}
print(diccionarioNuevo)
#Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#los diccionas pueden almacenar distintos tipos de datos
diccionario2 = {'Pablo':{'Edad':40, 'Altura':1.75}, 'Ariel':[40, 1.83], 'Osvaldo': [45, 1.85], 'Natalia': [35,1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre':'Lionel Messi', 'Edad':37, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo'},
    22: {'Nombre':'Lautaro Martinez', 'Edad':27, 'Altura': 1.74, 'Precio': '110 Millones', 'Posicion': 'Delantero'},
    23: {'Nombre':'Emiliano Martinez', 'Edad':32, 'Altura': 1.95, 'Precio': '30 Millones', 'Posicion': 'Arquero'},
    13: {'Nombre':'Cuti Romero', 'Edad':26, 'Altura': 1.85, 'Precio': '65 Millones', 'Posicion': 'Defensor'},
    20: {'Nombre':'Alexis Max Allister', 'Edad':25, 'Altura': 1.76, 'Precio': '75 Millones', 'Posicion': 'Mediocampista'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 30, 'Altura': 1.77, 'Precio': '20 Millones','Posicion': 'Delantero'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 30, 'Altura': 1.82, 'Precio': '30 Millones', 'Posicion': 'Mediocampista'},
    9: {'Nombre': 'Julian Alvarez', 'Edad': 24, 'Altura': 1.70, 'Precio': '80 Millones', 'Posicion': 'Delantero'},
    7: {'Nombre': 'Rodrigo de Paul', 'Edad': 30, 'Altura': 1.80, 'Precio': '40 Millones', 'Posicion': 'Mediocampista'}
}
print(seleccionArgentina)
print(seleccionArgentina[10])
print(seleccionArgentina.values())

for llave in seleccionArgentina.values():
    print(llave)

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Tenemos cargados en el diccionario de la seleccion la cantidad de jugadores: ',end=' ')
print(len(seleccionArgentina))

#PILAS USANDO LISTAS
pila = [1,2,3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#sacando elementos desde el final
elementoBorrado = pila.pop() #borra el ultimo elemento y lo guarda en la variable
print(f'Sacamlos el elemento borrado {elementoBorrado}')
print(f'La pila ahora queda asi: {pila}')

#COLAS CON LISTAS
#tipo FIFO (firts input /first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#sacamos elementos de la cola
seRetira=cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)