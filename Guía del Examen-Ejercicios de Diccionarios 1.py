#Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario con la frecuencia de cada letra en la cadena.

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


cadena = "Hola Mundo"
print("Frecuencia de letras:", contar_letras(cadena))
