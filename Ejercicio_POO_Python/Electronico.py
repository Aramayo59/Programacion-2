
from Producto import Producto  # Importa la clase Producto desde el archivo Producto.py

class Electronico(Producto):  # Define la subclase Electronico que hereda de Producto
    
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        # Método inicializador de la clase Electronico
        # Llama al método __init__ de la clase base (Producto) para inicializar atributos heredados
        super().__init__(nombre, precio, cantidad)
        self.marca = marca  # Atributo específico de Electronico: marca del producto electrónico
        self.modelo = modelo  # Atributo específico de Electronico: modelo del producto electrónico

    def mostrar_informacion(self):
        # Método para mostrar información del producto electrónico
        info_producto = super().mostrar_informacion()  
        # Obtiene la información básica del producto
        # Retorna la información completa, incluyendo marca y modelo del producto electrónico
        return info_producto + ", Marca: " + self.marca + ", Modelo: " + self.modelo
