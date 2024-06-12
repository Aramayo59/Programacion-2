# Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva cuántas veces aparece ese valor en la lista.

def contar_elemento(lista, valor):
    return lista.count(valor)


numeros = [1, 2, 3, 4, 5, 1, 2]
valor = 2
print("El valor", valor, "aparece", contar_elemento(numeros, valor), "veces")
