import random

def monty_hall(num_simulations, cambiarPuerta):
    victorias = 0

    for _ in range(num_simulations):
        # Escoger una puerta al azar para el premio
        premio = random.randint(1, 3)

        # Escoger una puerta al azar para la elección inicial del concursante
        primeraEleccion = random.randint(1, 3)

        # Monty abre una puerta que no tiene el premio ni la elección inicial del concursante
        puertasDisponibles = [1, 2, 3]
        puertasDisponibles.remove(premio)
        if primeraEleccion in puertasDisponibles:
            puertasDisponibles.remove(primeraEleccion)
        monty_abre = random.choice(puertasDisponibles)

        # Actualizar los conteos de victorias
        decisionFinal = list(set([1, 2, 3]) - set([primeraEleccion, monty_abre]))[0]

        if cambiarPuerta:
            if decisionFinal == premio:
                victorias += 1
        else:
            if primeraEleccion == premio:
                victorias += 1

    # Imprimir los resultados
    return [
        f"Victorias: {victorias} - {victorias/num_simulations}",
        f"Derrotas: {num_simulations - victorias} - {(num_simulations - victorias)/num_simulations}"
    ]

# Ejemplo de uso
def init():
    print("Simulacion de Monty Hall")
    sim = input("Numero de simulaciones: (1000/10000/100000): ").lower()
    cambiar = input("Cambiar de puerta? (s/n): ").lower()
    print("Configuracion de la simulacion: ")
    print(" - Simulaciones: " + sim)
    print(" - Cambiar de puerta: " + cambiar)
    seguir = input("Ejecutar simulacion? (s/n): ").lower()
    if(seguir == "s"):
        resultado = monty_hall(int(sim), cambiar == "s")
    else:
        print("Simulacion cancelada")
        return

    print("Resultado de la simulacion: ")
    print(" - " + resultado[0])
    print(" - " + resultado[1])

init()

#TODO add prints to show the results in iterations of monty_hall function