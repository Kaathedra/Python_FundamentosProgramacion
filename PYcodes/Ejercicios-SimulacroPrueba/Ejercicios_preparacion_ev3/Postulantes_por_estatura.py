clasifica = 0

rechazado = 0


while True:
    try:
        cant_postulantes = int(input("Ingrese la cantidad de postulantes: "))
        if cant_postulantes > 0:
            break
        else:
            print("Error: Ingresa un numero entero positivo.")
    except:
        print("Error: Ingresa solo numeros validos.")

for i in range(cant_postulantes):
    while True:
        try:
            estatura = float(input(f"Ingrese la estatura del postulante {i + 1} en metros: "))
        except:
            print("Error: Ingresa un numero valido")
            continue

        if estatura >= 1.65:
            print(f"El postulante {i +1} clasifica")
            clasifica += 1
            break
        elif 0 < estatura < 1.65:
            print(f"El postulante {i + 1} está fuera del rango de estatura.")
            rechazado += 1
            break
        else:
            print("No puedes ingresar una estatura negativa o cero.")


print(f'''
Postulantes clasificados: {clasifica}

Postulantes rechazados: {rechazado}
''')