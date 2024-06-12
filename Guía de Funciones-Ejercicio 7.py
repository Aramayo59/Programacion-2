# Contar letras: Crea una función que tome una cadena como entrada y devuelva un diccionario con el recuento de cada letra en la cadena.

def contar_letras(cadena):
    contador = {}
    for letra in cadena:
        if letra.isalpha():
            letra = letra.lower()
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
    return contador


texto = input("Ingresa una cadena de texto: ")
resultado = contar_letras(texto)
print("Recuento de letras:", resultado)
