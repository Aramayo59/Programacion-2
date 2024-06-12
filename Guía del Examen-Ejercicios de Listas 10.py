#Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.

def encontrar_indice(lista, valor):
    try:
        return lista.index(valor)
    except ValueError:
        return -1


numeros = [1, 2, 3, 4, 5]
valor = 3
print("El índice de", valor, "es:", encontrar_indice(numeros, valor))
