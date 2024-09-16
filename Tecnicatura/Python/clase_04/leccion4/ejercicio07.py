# Ejercicio 7: 
# Realiza un juego para adivinar un número. Para ello se debe generar un número aleatorio entre 1-100. Seguidamente
# solicitar más números al usuario indicando "es mayor" / "es menor" según sea el caso con respecto a N. El proceso termina
# cuando el usuario logra adivinar el valor de N. Finalmente, mostramos la cantidad de intentos realizados. 

import random
print('\t"Juego Adivina el numero (1-100)"')

aleatorio = random.randint(0, 100) # generamos un numero aleatorio
contador = 0

while True:
    numero = int(input('Digite un numero: '))
    contador += 1
    if numero > aleatorio:
        print('El valor ingresado es mayor, digita un numero menor')
        contador += 1
    elif numero < aleatorio:
        print('El valor ingresado es menor, digite un numero mayor')
        contador += 1
    else:
        print(f'Usted ha adivinado. El numero oculto era {aleatorio}')
        break # rompe el ciclo
print(f'\nNumero de intentos: {contador}')

