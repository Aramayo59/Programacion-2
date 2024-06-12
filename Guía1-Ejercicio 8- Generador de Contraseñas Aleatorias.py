# Escribe un programa en Python que genere una contraseña aleatoria para el usuario. La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.


import random
import string


def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña


contraseña = generar_contraseña()
print("Tu contraseña aleatoria es:", contraseña)
