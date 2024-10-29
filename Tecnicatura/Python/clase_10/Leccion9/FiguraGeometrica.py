from abc import ABC, abstractmethod   # importamos el metodo abstract base class, convierte una clase en abstracta

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validar_valores(alto):    
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el ancho: {ancho}')

    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')
    
    @abstractmethod
    def calcular_area(self):
        pass     # se utiliza para no implementarse aqui
    
    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    def _validar_valores(self, valor):   # Metodo encapsulado, esto se debe usar internamente en la clase padre
        return True if 0 < valor < 10 else False
    
