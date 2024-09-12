# Colecciones en PYTHON 

# Listas [ ]
# Tupas ( )
# Set { }
# Diccionarios { : , }

# Listas en Python. Estos son conjuntos de elementos. Son modificables (conocidos como arreglos o vectores), pueden tener diversos tipos de datos
# poseen un índice

nombres = ['Naty', 'Jose', 'Lautaro', 'Lily']
print('# Lista completa')
print(nombres, '\n')
print('# Mostramos la posicion 0 de la lista')
print(nombres[0], '\n')
print('# Mostramos el último elemento de la lista')
print(nombres[-1], '\n')
print('# Mostramos desde el índice 0 al 2, sin incluir este último')
print(nombres[0:2], '\n')
print("# Desde el inicio de la lista hasta la posición especificada, sin incluirlo")
print(nombres[:3],'\n')
print("# Desde el índice indicado hasta el final")
print(nombres[2:],'\n')

print('# Modificamos un valor')
nombres[3] = 'Estefania'
nombres[0] = 'Silvero'
print(nombres, '\n')

print('# Iteramos la lista')
for i in nombres:
    print(i)
else:
    print('Se acabaron los elementos de la lista', '\n')

print('# Preguntamos cuántos elementos tiene una lista')
print(len(nombres), '\n') # len nos devuelve la longitud

print('# Agregamos un elemento a nuestra lista')
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres, '\n')

print('# Insertar elementos en un índice especificado')
nombres.insert(1, 'Alberto')
nombres.insert(3, 'Debora')
print(nombres, '\n')

print('# Eliminar un elemento')
nombres.remove('Alberto')
print(nombres, '\n')

print('# Eliminar el último elemento')
nombres.pop()
print(nombres, '\n')

print('# Eliminar un elemento específico por índice')
del nombres[2]
print(nombres, '\n')

print('# Eliminar, borrar o limpiar todos los elementos de la lista')
nombres.clear()
print(nombres, '\n')

print('# Eliminar lista')
del nombres
print('\n')

# Tuplas en Python. Estas son inmutables, no se pueden modificar

print('# Definimos una Tupla')
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina, '\n')

print('# Mostramos la logintud')
print(len(cocina),'\n')

print('# Acceder a un elemento')
print(cocina[0])
print(cocina[-1], '\n')

print('# Acceder a un rango')
print(cocina[0:2], '\n')

# Una tupla necesita, aunque tenga un sólo elemento, de una coma. Caso contrario solo sería un String
verduras = ('papa',)

print('# Recorremos los elementos de la tupla')
for i in cocina:
    print(i, end= ' ') # usamos end para evitar el salto de línea que utiliza print
print('\n')

print('# Modificamos nuestra tupla de manera indirecta')
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print(cocina, '\n')

print('# Eliminamos la tupla', '\n')
del cocina

# Set (s) o Conjuntos

print('# Tipo Set - también conocido como Conjuntos')
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas, '\n')

print('# Revisamos si un elemento existe dentro del Set')
print('Jupiter' in planetas, '\n')

print('# Agregamos un elemento al Set ')
planetas.add('Tierra')  # en los Sets no podemos agregar elementos duplicados
print(planetas, '\n')

print('# Eliminar elementos del Set (Jupiter)') # esto puede arrojar un error si el elemento no existe
planetas.remove('Jupiter')  # esta función si no ingresamos de manera correcta el valor, no arrojará un error
print(planetas, '\n')

print('# Eliminar elementos del Set (con discard)') 
planetas.discard('tierra')  # la diferencia en esencia, es que uno nos arroja error, la otra función no
print(planetas, '\n')

print('# Limpiamos nuestro Set con clear') 
planetas.clear() 
print(planetas, '\n')

print('# Eliminamos el Set con del', '\n') 
del planetas 

# Diccionarios: están compuestos por dos elementos, una "llave y un valor"
# dict(key, value)

print('# Diccionarios') 
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Object Oriented Programming',
    'SABD': 'Database Management System'
}
print(diccionario, '\n')

print('# Ver la longitud de los elementos') 
print(len(diccionario), '\n')

print('# Accedemos a sus valores utilizando sus key []') 
print(diccionario['IDE'], '\n')

print('# Otro modo de accedes a los elementos del diccionario (get)') 
print(diccionario.get('SABD'))
print(diccionario.get('POO'), '\n')

print('# Modificamos el valor de un elemento del diccionario') 
diccionario['IDE']= 'Entorno de Desarrollo Integrado'
print(diccionario, '\n')

print('# Recorremos las llaves de un diccionario') 
for termino in diccionario:
    print(termino)
print('\n')

print('# Recorremos el diccionario utilizando items para visulizar los valores') 
for termino, valor in diccionario.items():
    print(termino, ': ', valor)
print('\n')

print('# Recorremos solo las keys del diccionario') 
for termino in diccionario.keys():
    print(termino) 
print('\n')

print('# Recorremos solo los values del diccionario') 
for termino in diccionario.values():
    print(termino) 
print('\n')

print('# Comprobamos la existencia de algún elemento') 
print('IDE' in diccionario, '\n')

print('# Agregamos un elemento al diccionario') 
diccionario['PK'] = 'Primary Key'
print(diccionario, '\n')

print('# Eliminar un elemento') 
diccionario.pop('SABD')
print(diccionario, '\n')

print('# Vaciar un diccionario') 
diccionario.clear()
print(diccionario, '\n')

print('# Eliminar un diccionario') 
del diccionario
print('\n')

# Concatenación de Listas
print('# Concatenación de Listas') 
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 1, 6]
lista3 = lista1 + lista2 # concatenacion
print(lista3, '\n')

print('# Utilizar la funcion extend') 
lista3.extend([7, 8, 9, 1])   # funcion extend
print(lista3, '\n')

print('# Utilizar la funcion index para conocer el índice en donde está ubicado un elemento') 
print(lista3.index(5), '\n') # nos arroja un error si el valor que buscamos no esta en la lista

print('# Contar cuantos veces se repite un elemento en una lista') 
print(lista3.count(1), '\n')

print('# Invertir nuestra lista') 
lista3.reverse()
print(lista3, '\n')

print('# Repetir una lista multiplicando sus elementos') 
lista = [1, 2, 3] * 2
print(lista, '\n')

# Métodos de ordenamiento
print('# Métodos de ordenamiento', '\n')

print('# Método sort')
lista3.sort()   # ordena ascendentemente
print(lista3, '\n')

print('# Método sort pero de mayor a menor')
lista3.sort(reverse= True)   # ordena descendentemente
print(lista3, '\n') 

# Más repaso de Tuplas
# Con las tuplas podemos usar: index, count, len
# Podemos transformar listas en tuplas y tuplas en listas
print('# Más repaso de Tuplas', '\n')

tupla = (4, 'hola', 6.78, [1, 2, 78], 4, 'hola')
print(tupla, '\n')


print('# Buscamos un elemento en la tupla')
print(4 in tupla, '\n')  # su respuesta es de tipo booleana

# Repaso de Set o conjunto
# Definir un conjunto
print('# Repaso de Conjuntos')
conjunto2 = set() #esta es la única forma de inicializar un conjunto y que esté vacío
conjunto1 = {'Hola'}  
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2, '\n')

conjunto1.add('bay')
print(conjunto1, '\n')

# Comprobamos la existencia de algun elemento en el conjunto
print('# Comprobamos la existencia o no de algun elemento en el conjunto')
print(3 not in conjunto1, '\n')

# Como hacer la igualdad de dos conjuntos
print('# Comparamos dos conjuntos')
print(conjunto2 == conjunto1, '\n')  #nos devolverá un booleano

# Operaciones con conjuntos
print('# Operaciones con Conjuntos')
# Union de Conjuntos
print('# Union de Conjuntos')
conjunto3 = conjunto1 | conjunto2
print(conjunto3, '\n')

# Interseccin
print('# Interseccion de conjuntos')
conjunto3 = conjunto1 & conjunto2  # almacenara el elemento que tienen en comun
print(conjunto3, '\n')


print('# Asigna el valor que esta en el conjunto 1 y no en el conjunto 2')
conjunto3 = conjunto1 - conjunto2  
print(conjunto3, '\n')

print('# Asigna el valor que esta en el conjunto 2 y no en el conjunto 1')
conjunto3 = conjunto2 - conjunto1  
print(conjunto3, '\n')

print('# Diferencia asimetrica - elementos que son diferentes entre ambos conjuntos')
conjunto3 = conjunto1 ^ conjunto2  
print(conjunto3, '\n')

print('# Determinar si un conjunto es subconjunto de otro')
conjunto3 = conjunto1 | conjunto2  
print(conjunto2.issubset(conjunto3)) #comprobacion booleana
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto2), '\n')


print('# Super Set - Tiene todos los datos de otro conjunto')
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3), '\n')

print('# Comprobar si los conjuntos son disconexos - que no compartin ningun elemento en comun')
print(conjunto1.isdisjoint(conjunto2), '\n')  # no hay cosas en comun

print('# Transformar un conjunto en inmutable', '\n')
conjunto1 = frozenset # esto hace que el conjunto sea inmutable

# Repaso Diccionarios
print('# Repaso Diccionarios')
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}

# Eliminar elemento
del(diccionarioNuevo['Azul'])

print('# Mostramos el diccionario')
print(diccionarioNuevo, '\n')

print('# Los diccionarios pueden almacenar diferentes tipos de datos')
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 167]}
print(diccionario2, '\n')

# Diccionario Seleccion Argentina
print('# Diccionario Seleccion Argentina')
seleccionArgentina = {
    10 : {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo Derecho'},
    11 : {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo Derecho'},
    21 : {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Medio Campo'},
    19 : {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensor'},
    1 : {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Arquero'},
    2 : {'Nombre': 'Cristian Romero', 'Edad': 29, 'Altura': 1.83, 'Precio': '8.7 millones', 'Posicion': 'Defensor'},
    8 : {'Nombre': 'Marcos Acuña', 'Edad': 31, 'Altura': 1.79, 'Precio': '10 millones', 'Posicion': 'Medio Campo'},
    6 : {'Nombre': 'Leandro Paredes', 'Edad': 28, 'Altura': 1.81, 'Precio': '14 millones', 'Posicion': 'Extremo Izquierdo'},
    7 : {'Nombre': 'Rodrigo De Paul', 'Edad': 33, 'Altura': 1.84, 'Precio': '19 millones', 'Posicion': 'Medio Campo'}
}
print(seleccionArgentina, '\n')

print('# Recorremos el diccionario usando un bucle for')
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print('\n')


print('# Longitud de nuestro diccionario')
print(len(seleccionArgentina), '\n')

# Metodo Pilas
print('# Utilizando el metodo pilas')
pila = [1, 2, 3]

print('# Agregar elemento a la pila por el final')
pila.append(4)
pila.append(5)
print(pila, '\n')

print('# Quitando elementos')
elementoBorrado = pila.pop()
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}', '\n')

# Colas con listas
# Estructura de datos de tipo fifo (first input / first output)
print('# Colas con listas')
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')

print('# Mostramos nuestra lista llamada cola')
print(cola, '\n')

print('# Sacamos elementos')
seRetira = cola.pop(0)
print(f'Se retira {seRetira}')
print(f'La lista queda asi: {cola}', '\n')

print('# Sacamos otro elementos')
seRetira = cola.pop(0)
print(f'Se retira {seRetira}')
print(f'La lista queda asi: {cola}', '\n')

# Clase 4

# Recorremos un diccionario
print('# Recorremos un diccionario con la interpolacion (f)')
for i in seleccionArgentina: 
    print(f'{i} -> {seleccionArgentina[i]}')