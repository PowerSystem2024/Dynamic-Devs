class Rectangle:
    """
    Esta clase contendrá 2 atributos: altura y base.
    Como métodos habrá uno para calcular el área utilidando la fórmula base * altura.
    Los datos como base y altura de cada objeto deben ser ingresados por el usuario.

    En este caso se opta por usar variables en inglés
    length = base
    height = altura
    """

    def __init__(self, length_, height_):
        self.length = length_
        self.height = height_

    def calculate_area(self):
        return self.length * self.height


# se usa un ciclo for para iterar 3 veces como pide el ejercicio, pero se hace uso de un único objeto
for i in range(1, 4):
    length = int(input(f'Base del rectángulo {i}: '))
    height = int(input(f'Altura del rectángulo {i}: '))
    rectangle = Rectangle(length, height)
    print(
        f'El área del rectángulo {i} que mide {rectangle.length} '
        f'de largo y {rectangle.height} de alto es {rectangle.calculate_area()}'
    )
