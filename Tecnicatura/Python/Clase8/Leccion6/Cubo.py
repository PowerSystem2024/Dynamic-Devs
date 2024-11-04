class Cubo:
    """
    Crear la clase cubo con los atributos, ancho, alto y profundiad, con un método calcular_volumen
    que tendra la formula: volumen = ancho *altura * profundidad. Que el usuario ingrese los valores
    """
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

ancho = int(input('Digite el ancho del cubo: '))
alto = int(input('Digite el alto del cubo: '))
profundidad = int(input('Digite la profundidad del cubo: '))

cubo1 = Cubo(ancho, alto, profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')