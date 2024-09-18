# Ejercicio 8: menú interactivo - Cajero Automático
# Hacer un programa que simule un cajero automático con un saldo inicial de U$1000 y con el siguiente menú
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 1000

while True:
    print('\t.:Menu:.')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input('Digite una opcion de menu: '))
    print()
    if opcion == 1:
        saldo = saldo + float(input('Digite el monto de dinero que desea ingresar a la cuenta: '))
        print(f'Saldo Ingresado con exito. El saldo en su cuenta es: U$ {saldo}')
    elif opcion == 2:
        retiro = float(input('Digite el monto de dinero que desea retirar: '))
        if retiro > saldo:
            print('Saldo insuficiente para realizar esta transacción') 
        else:
            saldo -= retiro
            print(f'Transaccion realizada con exito. El saldo en su cuenta es: U$ {saldo}')
    elif opcion == 3:
        print(f'El saldo en su cuenta es: U$ {saldo}')
    elif opcion == 4:
        print(f'Gracias por utilizar nuestros servicios')
        break
    else:
        print('Ha ingresado una opcion inválida')
