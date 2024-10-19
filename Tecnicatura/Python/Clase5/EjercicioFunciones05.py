"""Ejercicio %: Convertidor de temperaturas
Realizar dos funciones para convertir de grados celsius
a fahrenheit y viseversa, investigar las formulas

Funcion que convierte de celsius a fahrenheit
"""

def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

#Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f"{celsius} C a F -> {resultado:.2F}")

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} F a C -> {resultado:.2F}")