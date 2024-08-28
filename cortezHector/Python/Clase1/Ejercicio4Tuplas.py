# Dada la tupla (13, 1, 8, 3, 2, 5, 8,)
# crear una lista que incluya los números menores a 5
# Imprimir los valores
# Ejemplo: [1, 3, 2]

# variables necesarias
myTuple = (13, 1, 8, 3, 2, 5, 8,)
resultList = []

# recolectamos los valores menores a 5
for value in myTuple:
    if value < 5:
        resultList.append(value)

# mostramos la lista resultante por consola
print(resultList)
