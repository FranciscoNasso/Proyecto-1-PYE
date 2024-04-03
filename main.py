import random


def monty_hall(num_simulations, cambiarpuerta):
    victorias = 0

    for _ in range(num_simulations):
        # Escoger una puerta al azar para el premio
        premio = random.randint(1, 3)
        print("El auto esta en la puerta numero: " + str(premio) + "/3")

        # Escoger una puerta al azar para la elección inicial del concursante
        primeraeleccion = random.randint(1, 3)
        print("Concursante elije la puerta: " + str(primeraeleccion) + "/3")

        # Monty abre una puerta que no tiene el premio ni la elección inicial del concursante
        puertasDisponibles = [1, 2, 3]
        puertasDisponibles.remove(premio)
        if primeraeleccion in puertasDisponibles:
            puertasDisponibles.remove(primeraeleccion)
        monty_abre = random.choice(puertasDisponibles)
        print("Monty abre la puerta: " + str(monty_abre) + "/3")

        # Actualizar los conteos de victorias
        if cambiarpuerta:
            decisionfinal = list({1, 2, 3} - {primeraeleccion, monty_abre})[0]
            print("Concursante cambia la puerta: " + str(decisionfinal) + "/3")

        if cambiarpuerta:
            if decisionfinal == premio:
                victorias += 1
                print("Concursante gana!")
            else:
                print("Concursante no gana!")
        else:
            if primeraeleccion == premio:
                victorias += 1
                print("Concursante gana!")
            else:
                print("Concursante no gana!")

    # Imprimir los resultados
    return [
        f"Victorias: {victorias} - {victorias / num_simulations}",
        f"Derrotas: {num_simulations - victorias} - {(num_simulations - victorias) / num_simulations}"
    ]


# Ejemplo de uso
def init():
    print("Simulacion de Monty Hall")
    print("------------------------")
    print("A: 1000")
    print("B: 10000")
    print("C: 100000")
    simopt = input("Numero de simulaciones: ").lower()

    if simopt == "a":
        sim = 1000
    elif simopt == "b":
        sim = 10000
    else:
        sim = 100000

    cambiar = input("Cambiar de puerta? (s/n): ").lower()
    print("Configuracion de la simulacion: ")
    print(" - Simulaciones: " + str(sim))
    print(" - Cambiar de puerta: " + cambiar)
    seguir = input("Ejecutar simulacion? (s/n): ").lower()
    if seguir == "s":
        resultado = monty_hall(int(sim), cambiar == "s")
    else:
        print("Simulacion cancelada")
        return

    print(" - - - - - - - - - - - - - - - - ")

    print("Resultado de la simulacion: ")
    print(" - " + resultado[0])
    print(" - " + resultado[1])


init()
