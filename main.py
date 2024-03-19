import random

def monty_hall(num_simulations, cambiarPuerta):
    victorias = 0

    for _ in range(num_simulations):
        # Escoger una puerta al azar para el premio
        premio = random.randint(0, 2)

        # Escoger una puerta al azar para la elección inicial del concursante
        primeraEleccion = random.randint(1, 3)

        # Monty abre una puerta que no tiene el premio ni la elección inicial del concursante
        puertasDisponibles = [0, 1, 2]
        puertasDisponibles.remove(premio)
        if primeraEleccion in puertasDisponibles:
            puertasDisponibles.remove(primeraEleccion)
        monty_abre = random.choice(puertasDisponibles)


        # Actualizar los conteos de victorias
        if cambiarPuerta == 0:
            decisionFinal = list(set([1, 2, 3]) - set([primeraEleccion, monty_abre]))[0]
            if decisionFinal == premio:
                victorias += 1
        else:
            if decisionFinal == premio:
                victorias += 1

    # Imprimir los resultados
    print(f"Victorias con cambio de puerta: {victorias}")

# Ejemplo de uso
monty_hall(1000, 0)