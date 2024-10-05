class Cube:
    """
    Clase Cubo que tiene 3 atributos:
    ancho, alto y profundidad
    Contiene un método para calcular el volúmen
    y la fórmula es ancho * altura * profundidad
    length = ancho
    height = alto
    width = profundidad
    """

    def __init__(self, length_, height_, width_):
        self.length = length_
        self.height = height_
        self.width = width_

    def calculate_volume(self):
        return self.length * self.height * self.width


length = int(input('Ancho del cubo: '))
height = int(input('Altura del cubo: '))
width = int(input('Profundidad del cubo: '))
cube = Cube(length, height, width)
print(
    f'El volúmen del cubo que mide {cube.length} '
    f'de ancho x {cube.height} de alto x {cube.width} '
    f'de profundidad es {cube.calculate_volume()}'
)
