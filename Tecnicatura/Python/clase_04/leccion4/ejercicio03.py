# Ejercicio 3: insertar elementos y ordenarlos
# Pedir números e insertalos en una lista, cuando el usuario introduzca el número 0 el programa debe finalizar. 
# Por último, mostrar los números ordenados de menor a mayor.

lista = []
salir = False

while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)

lista.sort() # ordena la lista

print(f'\n Lista Ordenada: \n {lista}')

