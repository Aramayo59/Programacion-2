# Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un número validado como entero, el cual es ingresado por el usuario y se muestre el resultado del factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("Ingresa un número entero: "))
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
