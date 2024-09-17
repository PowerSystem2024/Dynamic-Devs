"""
Ejercicio 3: Funcion recursiva
imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
puede ser cualquier valor positivo, por ejemplo, si pasamos el valor 5 debe imprimir:
5,4,3,2,1
En caso de ser el numero 3 debe imprimir: 3,2,1
"""
def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")

imprimir_numeros_recursivos(5)
numero = int(input("Digite un numero positivo: "))
print(f"Los numeros que le siguen descendentemente al {numero} son: ")
resultado = imprimir_numeros_recursivos(numero)
