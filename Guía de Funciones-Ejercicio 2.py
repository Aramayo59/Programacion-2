
# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo


numeros = []
while True:
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    else:
        numeros.append(float(entrada))

maximo, minimo = calcularMaxMin(numeros)
print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)
