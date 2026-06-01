menu = '''
*** CONTROL TÉRMICO INDUSTRIAL ***
1. Registrar nueva lectura de temperatura
2. Mostrar cantidad de lecturas realizadas
3. Mostrar la temperatura mas baja registrada
4. Apagar sistema de monitoreo
'''

temperaturas = []

while True:
    print(menu)
    try:
        opc_menu = int(input("Ingrese la opcion: "))
        if 1 <= opc_menu <= 4:
            pass
        else:
            print("Error: Ingrese una opcion valida.")
            continue
    except:
        print("Ingrese un numero valido.")
        continue

    if opc_menu == 1:
        while True:
            try:
                reg_temp = float(input("Ingrese la temperatura a registrar: "))
                if reg_temp >= -273.15:
                    temperaturas.append(reg_temp)
                    print("Lectura guardada correctamente")
                    break
                else:
                    print("Error: ingresa un numero real positivo")
            except ValueError:
                print(f"Error ({ValueError}):Ingresa un numero real")
    elif opc_menu == 2:
        if len(temperaturas) == 0:
            print("No se han registrado lecturas.")
        else:
            print(f"Se han realizado {len(temperaturas)} lecturas.")
    elif opc_menu == 3:
        if len(temperaturas) == 0:
            print("No se han registrado lecturas.")
        else:
            print(f"Temperatura mas baja registrada: {min(temperaturas)}")
    elif opc_menu == 4:
        print("Saliendo del programa...")
        break