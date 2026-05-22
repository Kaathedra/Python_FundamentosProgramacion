menu = ''' *** Cine Estrella ***
        Bienvenido al sistem de venta de entradas del Cine Estrella
        1. Ver cuantas entradas quedan
        2. Comprar una cantidad de entradas
        3. Devolver entradas
        4. Salir del sistema'''

entradas_disponibles = 80

entradas_compradas = 0

entradas_devueltas = 0

while True:
    print(menu)
    try:
        opc_menu = int(input("Ingrese la opcion que desea realizar: "))
        if opc_menu == 1:
            print(f"Quedan {entradas_disponibles} entradas")
        elif opc_menu == 2:
            while True:
                try:
                    comprar_ticket = int(input("Ingrese la cantidad de entradas que desea: "))
                    if comprar_ticket > 0 and comprar_ticket <= entradas_disponibles:
                        entradas_disponibles -= comprar_ticket
                        entradas_compradas += comprar_ticket
                        print(f"\n{comprar_ticket} entradas compradas con exito.")
                        break
                    elif comprar_ticket > entradas_disponibles:
                        print(f"Error: La cantidad no puede exceder las entradas disponicles")
                    else:
                        print("Error: La cantidad no puede ser negativa o cero")
                except ValueError:
                    print("Error: Ingrese un numero entero positivo")
        elif opc_menu == 3:
            if entradas_compradas == 0:
                print("\n Error: No tienes entradas registradas a tu nombre para devolver.")
                continue
            
            while True:
                try:
                    devolver_ticket = int(input("Ingrese la cantidad de entradas que desea devolver: "))
                    if devolver_ticket > 0:
                        if devolver_ticket <= entradas_compradas:
                            entradas_disponibles += devolver_ticket
                            entradas_compradas -= devolver_ticket
                            entradas_devueltas += devolver_ticket
                            print(f"\n{devolver_ticket} entradas devueltas con exito.")
                        elif devolver_ticket == 0:
                            break
                        else:
                            print(f"Error: No puedes devolver mas entradas de las que ha comprado {entradas_compradas}")
                    else:
                        print("Error: La cantidad no puede ser negativa o cero")
                except ValueError:
                    print("Error: Ingrese un numero entero positivo")
        elif opc_menu == 4:
            print("\nGracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
            break
        else:
            print("Ingrese una opcion valida.")
    except ValueError:
        print("Error: El sistema solo considera numeros enteros.")