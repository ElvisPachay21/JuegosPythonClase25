from random import randint


numero_secreto = randint(0, 10)

def adivina_el_numero():
    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 0 y 10. ¿Puedes adivinar cuál es?") 
    
    intentos = 0 

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        distancia = abs(numero_secreto - intento)
        
        if intento < numero_secreto:
            if distancia <= 10:
                print("Demasiado bajo y estás cerca, intenta de nuevo.")
            else:
                print("Demasiado bajo y estás lejos, intenta de nuevo.")
        elif intento > numero_secreto:
            if distancia <= 10:
                print("Demasiado alto y estás cerca, intenta de nuevo.")
            else:
                print("Demasiado alto y estás lejos, intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_el_numero()
