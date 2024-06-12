#Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un diccionario con los números de 1 a n como claves y sus cuadrados como valores.

def diccionario_cuadrados(n):
    return {i: i**2 for i in range(1, n+1)}


n = 5
print("Diccionario de cuadrados:", diccionario_cuadrados(n))
