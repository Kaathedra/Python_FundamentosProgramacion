from random import randint
import math

low_limit = int(input("Ingrese el limite inferior: "))
top_limit = int(input("Ingrese el limite superior: "))

if low_limit >= top_limit:
    print("Error, el limite inferior debe ser menor al limite superior")
    exit()

num_secret = randint(low_limit, top_limit)

rango = top_limit - low_limit

if num_secret % 2 != 0:
        num_secret += 1

cant_intentos = max(2, round((math.log2(rango)) * 0.75))

intento_previo = None

for i in range(cant_intentos):
    if i == 0: msg = "Intente Adivinar. "
    else: msg = "Intente otra vez. "

    intentos_quedan = cant_intentos - i
    intento = int(input(f"{msg}. Tienes {intentos_quedan} intentos: "))

    if intento == num_secret:
        print(f"Felicitaciones, {num_secret} era el numero secreto: ")
        break

    if i < cant_intentos - 1:
        if intento < num_secret:
            print("El numero es mayor.")
        else:
            print("El numero es menor.")

        if intento_previo is not None:
            dist_actual = abs(intento - num_secret)
            dist_previa = abs(intento_previo - num_secret)

            close_to = intento if dist_actual < dist_previa else intento_previo
            far_to = intento_previo if dist_actual < dist_previa else intento
            print(f"Te daré una pista: El numero esta mas cerca de {close_to} que de {far_to}")
        intento_previo = intento
else:
    print(f"Perdiste. El numero era {num_secret}")