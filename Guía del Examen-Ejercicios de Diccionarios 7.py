# Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y devuelva la suma de todos los valores.
def sumar_valores(diccionario):
    return sum(diccionario.values())


diccionario = {'a': 1, 'b': 2, 'c': 3}
print("Suma de valores:", sumar_valores(diccionario))
