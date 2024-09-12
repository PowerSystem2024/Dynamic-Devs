import math  # importamos la clase math para usar la funcion sqrt (raiz cuadrada)
# Ejercicio Tuplas
numeros = (13, 1, 8, 3, 2, 5, 8)

lista = []
for i in numeros:
    if i < 5:
        lista.append(i)
print(lista)

# Ejercicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo

numero = int(input('Digite un numero positivo'))

while numero < 0:
    print('Error -> debería ser un número positivo: ')
    numero = int(input('Digite un numero positivo: '))

print(f'\nSu raiz cuadrarra es: {math.sqrt(numero):.2f}')
