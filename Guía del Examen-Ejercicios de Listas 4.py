# Elementos mayores que un valor: Escribe una función que tome una lista de números y un valor n, y devuelva una nueva lista con los elementos mayores que n.

def mayores_que(lista, n):
    return [x for x in lista if x > n]


numeros = [1, 2, 3, 4, 5]
n = 3
print("Elementos mayores que", n, ":", mayores_que(numeros, n))
