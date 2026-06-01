atleta_master = []
atleta_pro = []

while True:
    try:
        ingreso_atleta = int(input("Ingresa la cantidad de atletas a registrar: "))
        if ingreso_atleta > 0:
            break
        else:
            print("Error: El numero no puede ser 0 o negativo.")
    except ValueError:
        print("Por favor, ingresa un numero entero valido")
        
for i in range(ingreso_atleta):
    while True:
            code_atleta = input(f"Ingresa un codigo para identificar al atleta {i + 1} (El codigo debe estar en mayusculas y ser de 6 o mas caracteres): ").strip()
            if len(code_atleta) >= 6 and code_atleta.isupper() and " " not in code_atleta:
                break
            else:
                print("Ingreso invalido. Por favor respeta los requerimientos.")
    while True:
        try:
            edad_atleta = int(input(f"Ingresa la edad del atleta {code_atleta}: "))
            if edad_atleta < 0 or edad_atleta > 99:
                print("Error biometrico: Ingresa una edad valida de deportista para continuar")
            else:
                if edad_atleta > 30:
                    atleta_master.append(code_atleta)
                else:
                    atleta_pro.append(code_atleta)
                break
        except ValueError:
                        print("Error: Ingresa un numero entero valido")
print(f"¡El CAR cuenta con {len(atleta_master)} atletas Master y {len(atleta_pro)} atletas pro!¡Entrenamiento autorizado!")