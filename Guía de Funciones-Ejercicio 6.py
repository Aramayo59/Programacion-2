# Suma de pares: Escribe una función que tome una lista de números y devuelva la suma de los números pares en la lista.

def suma_pares(lista):
    suma = sum(num for num in lista if num % 2 == 0)
    return suma


numeros = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
resultado = suma_pares(numeros)
print("La suma de los números pares es:", resultado)
