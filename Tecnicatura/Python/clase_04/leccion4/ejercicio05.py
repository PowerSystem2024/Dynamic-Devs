# Ejercicio 5: factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo

numero = int(input('Digite un numero: '))

while numero < 0:  # mientras el numero sea negativo
    print('Error -> el numero debe ser positivo')
    numero = int(input('Digite un numero: '))

factorial = 1 # variable para calcular el factorial

for i in range(1, numero+1):
    factorial *= i
print(f'\nEl factorial del numero {numero} ingresado es: {factorial}')
