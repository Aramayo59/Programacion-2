# Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.



import re


def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not re.search("[A-Z]", contraseña):
        return False
    if not re.search("[a-z]", contraseña):
        return False
    if not re.search("[0-9]", contraseña):
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", contraseña):
        return False
    return True

contraseña = input("Ingresa una contraseña: ")


if validar_contraseña(contraseña):
    print("La contraseña es válida")
else:
    print("La contraseña no es válida")
