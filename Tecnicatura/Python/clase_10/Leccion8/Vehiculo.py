class Vehiculo: 
    '''
    Definir una clase padre llamada vehiculo y dos clases hijas llamadas Auto, Bicicleta, las cuales heredan de la clase padre vehiculo. La clase padre debe tener los siguientes atributos y metodos:
    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Metodos(__init__() y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad(km/hs))
    -Metodos(__init__() y __str__())

    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montana/etc.))
    -Metodos(__init__() y __str__())

    Crear un objeto de cada clase
    '''
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):   # metodo dunder, devuelve un str
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + ', velocidad (km/hs): ' + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ', tipo: ' + self.tipo


# primer objeto de la clase vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# segundo objeto de la clase Auto
auto = Auto('Amarillo', 4, 120)
print(auto)

# tercer objeto de la clase Bicicleta
bicicleta = Bicicleta('Azul', 2, 'Urbana')
print(bicicleta)