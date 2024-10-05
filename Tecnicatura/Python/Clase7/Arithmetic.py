class Arithmetic:
    """
    Esta clase se encargará de realizar operaciones aritmeticas básicas,
    tales como sumar, restar, multiplicar, dividir y más.
    """

    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    def addition(self):
        return self.value_a + self.value_b

    def subtraction(self):
        return self.value_a - self.value_b

    def multiplication(self):
        return self.value_a * self.value_b

    def division(self):
        return self.value_a / self.value_b


arithmetic1 = Arithmetic(2, 5)
print(arithmetic1.addition())
arithmetic2 = Arithmetic(6, 10)
print(arithmetic2.addition())

'''
Clase 7: uso de la palabra self y creación de atributos
para un objeto
'''
# forma distinta de llamar al método de un objeto haciendo
# uso de su clase
Arithmetic.addition(arithmetic1)  # obsoleto en la actualidad

'''
Crear variables superficiales para un único objeto:
esto permite la creación de nuevos atributos a un objeto único
no así para el resto de los objetos que son parte de la misma clase
'''
arithmetic1.value_c = 8
print(f'Valor de C para el objeto arithmetic1: {arithmetic1.value_c}')
# print(f'Valor de C para el objeto arithmetic2: {arithmetic2.value_c}') # esto no es posible
print()
print(f'Suma entre {arithmetic1.value_a} + {arithmetic1.value_b} = {arithmetic1.addition()}')
print(f'Resta entre {arithmetic1.value_a} - {arithmetic1.value_b} = {arithmetic1.subtraction()}')
print(f'Multiplicación entre {arithmetic1.value_a} x {arithmetic1.value_b} = {arithmetic1.multiplication()}')
print(f'División entre {arithmetic1.value_a} / {arithmetic1.value_b} = {arithmetic1.division()}')
