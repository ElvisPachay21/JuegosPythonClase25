def laberinto():
    laberinto = {"entrada": { "norte": "pasillo", "sur": None,  "este": None, "oeste": None}, "pasillo": {"norte": "salida", "sur": "entrada", "este": "cuarto oscuro", "oeste": "bodega" },"cuarto oscuro": {"norte": None, "sur": None, "este": "biblioteca",  "oeste": "pasillo" },
                 "salida": { "norte": None,"sur": "pasillo","este": None, "oeste": None},
                 "bodega": {"norte": None,"sur": "sala de trampas", "este": "pasillo", "oeste": None },
                 "sala de trampas": {"norte": "bodega",  "sur": None,  "este": "sala secreta","oeste": None},
                 "sala secreta": {"norte": None, "sur": None, "este": None, "oeste": "sala de trampas"}, 
                 "biblioteca": {"norte": None, "sur": None, "este": None,"oeste": "cuarto oscuro"}}
    
    posicion_actual = "entrada"
    print("¡Bienvenido al laberinto! Tienes que encontrar la salida.")

    while True:
        direcciones = [d for d in laberinto[posicion_actual].keys() if laberinto[posicion_actual][d] is not None]
        direccion = input(f"Estás en {posicion_actual}. Puedes ir hacia: {', '.join(direcciones)}. ¿Hacia dónde vas? ").lower()

        if direccion in laberinto[posicion_actual] and laberinto[posicion_actual][direccion]:
            posicion_actual = laberinto[posicion_actual][direccion]
            if posicion_actual == "salida":
                print("¡Felicidades, encontraste la salida!")
                break
        else:
            print("No puedes ir en esa dirección, intenta de nuevo.")

laberinto()