from random import randint

while True:
    try:
        low_limit = int(input("Ingrese el limite inferior: ")) # Solicitamos el limite inferior

        top_limit = int(input("Ingrese el limite superior: ")) # Solicitamos el limite superior

        if low_limit < top_limit:
            break
        else:
            print("Error. El limite superior no puede ser menor al inferior.")
    except ValueError:
        print("Error: Ingresa numeros enteros.")

num_random = randint(low_limit, top_limit)

num_ajustado = (num_random // 5) * 5

num_de_intentos = 1

if num_ajustado == 0:
    num_ajustado = 5

while True:
    try:
        intento = int(input("Intente adivinar: "))
        if intento != num_ajustado:
            num_de_intentos += 1
            pass
        else:
            print(f"Felicidades has adiviniado en tu intento N° {num_de_intentos}!")
            break
    except ValueError:
        print("Por favor solo ingresa nuemros enteros.")