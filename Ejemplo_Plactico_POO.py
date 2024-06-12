class Vehiculo:  # Crear nuestra CLASE PADRE
    def __init__(self, marca, anio, patente, color):  # CONSTRUCTOR
        self.marca = marca
        self.anio = anio
        self.patente = patente
        self.color = color

    # Métodos/funciones de acceso a los atributos
    def getPatente(self):
        return self.patente

    def getColor(self):
        return self.color

    def getMarca(self):
        return self.marca

    def getAnio(self):
        return self.anio

    # Método para mostrar la info del objeto en consola
    def mostrarInfoVehiculo(self):
        print("\nLos datos ingresados son:")
        print(f"Patente: {self.getPatente()}")
        print(f"Marca: {self.getMarca()}")
        print(f"Año: {self.getAnio()}")
        print(f"Color: {self.getColor()}")

# Solicitar el ingreso de los atributos
patente = input("Ingrese Patente: ")
marca = input("Ingrese la marca: ")
anio = input("Ingrese el año: ")
color = input("Ingrese el color: ")

# Crear una instancia de Vehiculo con los atributos ingresados
vehiculo = Vehiculo(marca, anio, patente, color)
vehiculo.mostrarInfoVehiculo()
