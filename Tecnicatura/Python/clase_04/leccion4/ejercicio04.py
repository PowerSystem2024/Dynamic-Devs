# Ejercicio 4: sumar números pares dentro de un rango
# Hacer un programa para q sumar números pares dentro de un rango. Ej:
# suma de números pares del 2 al 30. Suma = 240

a = int(input('Digite de donde va a comenzar la suma: '))
b = int(input('Digite hasta donde quiere llegar a sumar: '))
suma = 0

for i in range(a, b+1):
    if i % 2 == 0:
        suma += i
    
print(f'\nLa suma de los numeros pares es: {suma}')