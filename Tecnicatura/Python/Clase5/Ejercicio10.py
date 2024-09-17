#Ejercicio 10: No repetir caracteres
"""
Hacer un programa que pida una cadena por teclado, luego
meter los caracteres en una lista sin repetir caracteres
"""
cadena = input("Digite una cadena: ")
lista = []
for i in cadena:
    if i not in lista: #Si el caracter aun no esta en la lista
        lista.append(i) #agreganis a la lista
print(f"\nLista de caracteres sin repetir ninguno: \n {lista}")