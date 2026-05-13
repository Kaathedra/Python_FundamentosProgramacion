from random import randint

low_limit = int(input("Ingrese el limite inferior: "))
top_limit = int(input("Ingrese el limite superior: "))

if low_limit >= top_limit:
    print("Error, el limite inferior debe ser menor al limite superior")
    exit()

num_secret = randint(low_limit, top_limit)

if num_secret % 2 != 0:
    if num_secret == low_limit:
        num_secret += 1
    else:
        num_secret -= 1

cant_intentos = max(1, round((top_limit - low_limit) / 5))

intento = int(input(f"Intenta adivinar (te quedan {cant_intentos} intentos): "))

while (intento != num_secret) and cant_intentos > 1:
    print(f"{intento} no es el numero secreto")
    cant_intentos -= 1
    # --- intento_previo = intento ---
    intento = int(input(f"Intenta adivinar (te quedan {cant_intentos} intentos): "))
    # Terminar parte de las pistas #

if intento == num_secret:
    print(f"Felicitaciones {intento} es el numero secreto!")
else:
    print(f"Perdiste. El número secreto era {num_secret}")