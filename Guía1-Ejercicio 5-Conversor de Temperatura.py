# Mejora el programa de conversión de temperatura que escribiste anteriormente para que permita al usuario elegir entre convertir de grados Celsius a grados Fahrenheit o viceversa.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


opcion = input("¿Deseas convertir de Celsius a Fahrenheit (C) o de Fahrenheit a Celsius (F)? Ingresa C o F: ")

if opcion.upper() == "C":
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print("La temperatura en grados Fahrenheit es:", fahrenheit)
elif opcion.upper() == "F":
    fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print("La temperatura en grados Celsius es:", celsius)
else:
    print("Opción no válida")
