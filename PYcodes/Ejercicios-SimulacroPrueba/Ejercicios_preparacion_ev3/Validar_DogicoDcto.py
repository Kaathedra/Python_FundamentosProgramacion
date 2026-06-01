cod_validos = 0
cod_invalido = 0

while True:
    try:
        cant_codes = int(input("Ingrese la cantidad de codigos a verificar: "))
        if cant_codes > 0:
            break
        else:
            print("Error: La cantidad no puede ser negativa o cero.")
    except:
        print("Error: Ingresa un numero entero valido.")

for i in range(cant_codes):
    while True:
        try:
            code = int(input(f"Ingrese el codigo {i + 1}: "))
            if code % 2 == 0 and code > 0:
                print("Codigo Valido. Descuento aplicado.")
                cod_validos += 1
            else:
                print("Codigo Invalido o expirado.")
                cod_invalido += 1
            break
        except:
            print("Error: Ingresa un numero valido.")

print(f"""
Se ingresaron {cod_validos} codigos validos
Se ingresaron {cod_invalido} codigos invalidos
""")