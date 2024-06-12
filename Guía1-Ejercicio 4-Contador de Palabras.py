# Desarrolla un programa en Python que solicite al usuario que ingrese una frase y luego cuente y muestre el número de palabras en esa frase.

frase = input("Ingresa una frase: ")


pal = frase.split()
num_de_pal = len(pal)


print("El número de palabras en la frase es:", num_de_pal)

