# Palíndromo: Escribe una función que determine si una palabra o frase es un palíndromo (selee igual de adelante hacia atrás que de atrás hacia adelante), ignorando espacios y signos de puntuación.


def es_palindromo(frase):
    frase = ''.join(e for e in frase if e.isalnum()).lower()
    return frase == frase[::-1]


texto = input("Ingresa una palabra o frase: ")
if es_palindromo(texto):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
