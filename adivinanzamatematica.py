import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 3

    print("¡Bienvenido al juego de adivinanza!")
    print("Adivina el número entre 1 y 100.")
    
    while intentos_restantes > 0:
        try:
            intento = int(input("Ingresa tu intento: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if intento == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            break
        else:
            distancia = abs(numero_secreto - intento)
            if distancia <= 10:
                print("¡Muy cerca!")
            elif distancia <= 20:
                print("Cerca.")
            else:
                print("Muy lejos.")
                
            intentos_restantes -= 1
            print(f"Intentos restantes: {intentos_restantes}")

    if intento != numero_secreto:
        print(f"Lo siento, has usado todos tus intentos. El número secreto era {numero_secreto}.")


juego_adivinanza()
