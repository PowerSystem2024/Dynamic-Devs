# Los conjuntos o Set son un tipo de dato el cual no permite duplicados.
# En python los sets no contene índice y al consultar el conjunto, en cada llamado
# el orden será diferente

# declaramos un set
mySet = {"value 1", "value 2", "value 3"}
print(len(mySet))  # longitud del set
print(mySet)  # contenido del set

# comprobar si un elemento existe dentro del set
print("value 1" in mySet)  # devuelve true
print("value x" in mySet)  # devuelve false

# agregar un elemento
mySet.add("value 4")
print(mySet)  # ahora aparece el valor 4

# remover un elemento
mySet.remove("value 1")
print(mySet)  # el valor 1 ha sido removido
mySet.discard("value 3")
print(mySet)  # el valor 3 ha sido removido

# limpiar los elementos del set
mySet.clear()
print(mySet)  # devuelve -> set() como respuesta

# repaso y nuevos conceptos de las listas
myList = ["Hola", "Mundo"]

# agregar más elementos a la lista
myList.append([1, 2, 3])
myList.append(True)
myList.append(3.14)

# concatenación de listas
list1 = [3, 2, 1]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# agregar de a varios elementos a una lista
# y los agrega al final
list3.extend([9, 8, 7])
print(list3)

# en base a un elemento de la lista, obtener su índice
# si el valor no existe en la lista, da error
print(list3.index(7))

# comprobar si un elemento aparece más de una vez en
# una lista
# devuelve la cantidad de veces que ese valor se repite
print(list3.count(6))

# multiplicar una lista (cuantificar sus valores)
print(myList)  # output -> ['Hola', 'Mundo', [1, 2, 3], True, 3.14]
myList = myList * 2
print(myList)  # output -> ['Hola', 'Mundo', [1, 2, 3], True, 3.14, 'Hola', 'Mundo', [1, 2, 3], True, 3.14]

# métodos de ordenamiento
list3.sort()  # de menor a mayor
print(list3)
list3.sort(reverse=True)  # de mayor a menor
print(list3)
