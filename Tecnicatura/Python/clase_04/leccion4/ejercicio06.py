# Ejercicio 6: tabal de multiplicar
# Hacer un programa que pida un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10. 
# Por ejemplo: si digita el 5 la lista tendrá: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

numero = int(input('Digite un numero: '))
lista = []   # definimos la lista
for i in range(1, 11):
    lista.append(i*numero)

print(f'\nTabla de multiplicar del {numero}: \n{lista}')

# Para ver con formato de tabla de multiplicar
print('\n# Mostramos con formato de tabla de multiplicar')
for i in range(1, 11):
    print(f'{numero} x {i} = {i*numero}')