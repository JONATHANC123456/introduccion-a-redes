import random

# Tupla con las opciones (no pueden modificarse)
opciones = ("piedra", "papel", "tijera")

# Diccionario que indica qué opción gana a cuál
ganador = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel"
}

print("===== JUEGO PIEDRA, PAPEL O TIJERA =====")

# Se juegan 5 partidas
for ronda in range(1, 6):

    print("\nPartida", ronda)

    usuario = input("Elige piedra, papel o tijera: ").lower()

    # Validar la opción ingresada
    if usuario not in opciones:
        print("Opción no válida.")
        continue

    computadora = random.choice(opciones)

    print("Computadora eligió:", computadora)

    if usuario == computadora:
        print("¡Empate!")

    elif ganador[usuario] == computadora:
        print("¡Ganaste!")

    else:
        print("¡Perdiste!")

print("\nFin del juego. Se jugaron las 5 partidas.")
