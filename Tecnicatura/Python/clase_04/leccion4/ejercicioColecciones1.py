# Ejercicio 1: eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación elimine
# los elementos repetidos, por último mostrar la lista.

# Creamos una lista
lista = [1, 2, 3, "Jose", 7, 7, 3, "Alberto", 1, "Jose", 2, "Alberto"]
# conjunto = set(lista) # convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) # convertimos el conjunto a una lista
lista = list(set(lista)) # conversion realizada en una sola linea de codigo (eficiente)
print(lista)