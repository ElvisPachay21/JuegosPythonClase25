import random

def juego_adivinanza_palabra():
    palabras = {"python": "La palabra está relacionada con programación.",
        "zebra": "Es un animal que vive en África.",
        "mango": "Es una fruta tropical.",
        "luna": "Es el satélite natural de la Tierra."}
    
    palabra_secreta, pista = random.choice(list(palabras.items()))
    letra_inicial = palabra_secreta[0]
    intentos_restantes = 3

    print("¡Bienvenido al juego de adivinanza!")
    print("Adivina la palabra secreta.")
    print(f"Pista: {pista}")
    print(f"La primera letra de la palabra es: '{letra_inicial}'")
    
    while intentos_restantes > 0:
        intento = input("Ingresa tu intento: ").strip().lower()

        if intento == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra.")
            break
        else:
            print("Incorrecto.")
            intentos_restantes -= 1 
            print(f"Intentos restantes: {intentos_restantes}")

    if intento != palabra_secreta:
        print(f"Lo siento, has usado todos tus intentos. La palabra secreta era '{palabra_secreta}'.")

juego_adivinanza_palabra()
