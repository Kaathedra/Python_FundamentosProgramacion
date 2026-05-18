ingreso_permitido = 0

ingreso_denegado = 0

while True:
    try:
        cant_personas = int(input("Ingrese la cantidad de personas: "))
        if cant_personas > 0:
            break
        else:
            print("El numero no puede ser negativo o cero")
    except ValueError:
        print("Ingrese un numero entero")

for i in range(cant_personas):
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad < 0:
                print("La edad no puede ser negativa")
                continue
            if edad < 18:
                print("Ingreso denegado")
                ingreso_denegado += 1
            else:
                print("Ingreso permitido")
                ingreso_permitido += 1
            break
        except ValueError:
            print("Ingrese una edad valida")

print(f'''
    Ingresos permitidos: {ingreso_permitido}

    Ingresos denegados: {ingreso_denegado}
''')