# Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el valor máximo y el mínimo de la lista.

def max_min(lista):
    return max(lista), min(lista)


numeros = [1, 2, 3, 4, 5]
maximo, minimo = max_min(numeros)
print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)
