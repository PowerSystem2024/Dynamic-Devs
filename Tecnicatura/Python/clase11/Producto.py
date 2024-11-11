class Producto:
     contador_productos = 0
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self,precio):
        self._precio = precio

    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    producto3 = Producto('Remera', 80.00)
    producto4 = Producto('short', 120.00)