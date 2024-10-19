# Ejercicio 1: llenar una lista
# llenar una lista con los números del 1 al 50, luego mostrar la lista con el bucle for de la siguiente manera:
# 1-2-3-4-5...-50

# Creamos la lista
# lista = []
# i = 1
# while i <= 50:
#     lista.append(i)
#     i += 1

lista = list(range(1, 51))

for i in lista:
    print(i, end='-')