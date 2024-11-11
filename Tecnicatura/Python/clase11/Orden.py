from Producto import Producto
class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
       Orden.contador_ordenes += 1
       self.id_orden = orden.contador_ordenes
       self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto) # Para agregar un nuevo producto

    def calcular_total(self):
        total = 0 # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()+'|'
        return f'Orden: {self.id_orden}, \nProducto: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)
    productos1 = [producto1,producto2]
    orden1 = Orden(productos1)
    print(orden1)
    producto3 = Producto('Remera', 80.00)
    print(producto3)
    producto4 = Producto('short', 120.00)
    print(producto4)
    productos2 = [producto3, producto4]
    orden2 = Orden(productos2)
    print(orden2)