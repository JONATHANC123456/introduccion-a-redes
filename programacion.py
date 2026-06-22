import random

opciones = ["piedra", "papel", "tijera"]

# Elección del usuario
usuario = input("Elige piedra, papel o tijera: ").lower()

# Elección computadora
computadora = random.choice(opciones)

print("Computadora eligió:", computadora)

# Determinar ganador
if usuario == computadora:
    print("¡Empate!")
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste!")
elif usuario in opciones:
    print("¡Perdiste!")
else:
    print("Opción no válida.")