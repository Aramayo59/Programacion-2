
from Producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        info_producto = super().mostrar_informacion()
        return info_producto + ", Fecha de expiración: " + self.fecha_expiracion
