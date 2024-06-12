# Juego de Ahorcado: Crea un juego de ahorcado donde el jugador debe adivinar una palabra oculta antes de que se agoten los intentos. Puedes hacerlo con una lista predefinida de palabras.


import random


palabras = ["python", "programacion", "desarrollo", "tecnologia", "codigo"]


palabra_secreta = random.choice(palabras)
letras_adivinadas = ['_'] * len(palabra_secreta)
intentos = 6

print("¡Bienvenido al juego del ahorcado! Adivina la palabra.")


while intentos > 0 and '_' in letras_adivinadas:
    print(" ".join(letras_adivinadas))
    print(f"Te quedan {intentos} intentos.")
    letra = input("Ingresa una letra: ").lower()
    if letra in palabra_secreta:
        for i, char in enumerate(palabra_secreta):
            if char == letra:
                letras_adivinadas[i] = letra
    else:
        intentos -= 1

if '_' not in letras_adivinadas:
    print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
else:
    print("Lo siento, te has quedado sin intentos. La palabra era:", palabra_secreta)
