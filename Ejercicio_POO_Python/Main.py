from Electronico import Electronico
from Alimento import Alimento


electro1 = Electronico("Laptop", 1200, 10, "Dell", "XPS 15")
electro2 = Electronico("Smartphone", 800, 25, "Samsung", "Galaxy S21")
electro3 = Electronico("Televisor", 1500, 5, "Sony", "Bravia X90J")

alimento1 = Alimento("Manzana", 0.5, 50, "2024-12-31")
alimento2 = Alimento("Pan", 1.2, 100, "2024-06-15")
alimento3 = Alimento("Leche", 0.9, 30, "2024-07-01")


print(electro1.mostrar_informacion())
print(electro2.mostrar_informacion())
print(electro3.mostrar_informacion())

print(alimento1.mostrar_informacion())
print(alimento2.mostrar_informacion())
print(alimento3.mostrar_informacion())