# Ejercicio 1
# Iterar una lista de 0 a 10, imprimir números divisibles por 3

print('# Numeros divisibles por 3 en un rango de 0 a 10')
for i in range(11):
    if i % 3 == 0:
        print(i)


# Ejercicio 2
# Crear un rango de numeros desde el 2 al 6 e imprimirlos en pantalla
print('# Numeros en un rango de 2 a 6')
for i in range(2, 7):
    print(i)

# Ejercicio 3
# Crear un rango de numeros desde el 2 al 6 e imprimirlos en pantalla
print('# Numeros un rango de 3 a 10, con incremento de 2 en 2')
lista = list(range(3, 11, 2))
for i in lista:
    print(i)