import random as ran

numero_secreto = ran.randint(1, 100)
intentos_maximos = 5

intentos_realizados = 0

print(f"¡Adivina el número secreto (1-100)! Tienes {intentos_maximos} intentos.")

while intentos_realizados < intentos_maximos:
    intento = int(input(f"Intento {intentos_realizados + 1}: Ingresa tu número: "))
    intentos_realizados += 1
    
    if intento == numero_secreto:
        puntuacion = (intentos_maximos - intentos_realizados + 1) * 100
        print(f"¡Felicidades! {intento} era el número secreto.")
        print(f"Puntuacion: {puntuacion}")
        break 
    if intento < numero_secreto:
        print(f"'{intento}' es muy bajo. ↓")
    else:
        print(f"'{intento}' es muy alto. ↑")

if intento != numero_secreto:
    print(f"GAME OVER. El número era {numero_secreto}.")
    print("Puntuacion: 0 ptos. Mejor suerte a la proxima.")