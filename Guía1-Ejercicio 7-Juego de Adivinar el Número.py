# Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo. El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo. El juego debe continuar hasta que el jugador adivine correctamente el número.



import random


numero_secreto = random.randint(1, 100)


adivinado = False

print("¡Bienvenido al juego de adivinar el número! Intenta adivinar el número entre 1 y 100.")


while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    if intento < numero_secreto:
        print("Demasiado bajo")
    elif intento > numero_secreto:
        print("Demasiado alto")
    else:
        print("¡Felicidades! Adivinaste el número.")
        adivinado = True
