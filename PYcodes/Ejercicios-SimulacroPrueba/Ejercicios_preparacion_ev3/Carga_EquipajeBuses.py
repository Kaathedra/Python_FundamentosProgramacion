equipaje_aceptado = 0
equipaje_rechazado = 0

while True:
    try:
        cant_equipajes = int(input("Ingrese la cantidad de equipaje a registrar: "))
        if cant_equipajes > 0:
            break
        else:
            print("Error: La cantidad no puede ser cero o negativa.")
    except ValueError:
        print("Error: Ingrese un numero entero valido")
for i in range(cant_equipajes):
    while True:
        try:
            peso_equipaje = float(input(f"Ingrese el peso del equipaje {i + 1} en Kg: "))
            if peso_equipaje <= 0:
                print("Error de Ingreso (cero o negativo)")
                continue
            elif peso_equipaje > 23:
                print("Exceso de peso. No permitido")
                equipaje_rechazado += 1
            else:
                print("Equipaje aceptado!")
                equipaje_aceptado += 1
            break
        except ValueError:
            print("Ingresa un numero acorde al formato solicitado")

print(f'''  
Se aceptaron {equipaje_aceptado} equipajes.
Se rechazaron {equipaje_rechazado} equipajes.
''')