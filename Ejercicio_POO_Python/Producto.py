
class Producto:
 # Método inicializador que se ejecuta al crear una nueva instancia de la clase

    def __init__(self, nombre, precio, cantidad):
       # Atributos de instancia: se asignan los valores de los parámetros a los atributos del objeto
        
        self.nombre = nombre  # Nombre del producto
        self.precio = precio # Precio del producto
        self.cantidad = cantidad # Cantidad disponible del producto
     # Método para mostrar la información del producto
    def mostrar_informacion(self):
        # Retorna una cadena con la información del producto, formateando los valores de los atributos
        return "Producto: " + self.nombre + ", Precio: " + str(self.precio) + ", Cantidad: " + str(self.cantidad)
