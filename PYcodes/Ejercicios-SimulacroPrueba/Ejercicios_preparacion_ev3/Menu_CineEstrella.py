import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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
    clear_screen()
    print(menu)
    try:
        opc_menu = int(input("Ingrese la opcion que desea realizar: "))
        if opc_menu == 1:
            print(f"\nQuedan {entradas_disponibles} entradas")
            input("\nPresione [ENTER] para volver al menú.")
            clear_screen()
        elif opc_menu == 2:
            while True:
                try:
                    comprar_ticket = int(input("\nIngrese la cantidad de entradas que desea: "))
                    if comprar_ticket > 0 and comprar_ticket <= entradas_disponibles:
                        entradas_disponibles -= comprar_ticket
                        entradas_compradas += comprar_ticket
                        print(f"\n{comprar_ticket} entradas compradas con exito.")
                        input("\nPresione [ENTER] para volver al menú.")
                        clear_screen()
                        break
                    elif comprar_ticket > entradas_disponibles:
                        print(f"\nError: La cantidad no puede exceder las entradas disponibles")
                    else:
                        print("\nError: La cantidad no puede ser negativa o cero")
                        input("\nPresione [ENTER] para volver.")
                        continue
                except ValueError:
                    print("\nError: Ingrese un numero entero positivo")
        elif opc_menu == 3:
            if entradas_compradas == 0:
                print("\n Error: No tienes entradas registradas a tu nombre para devolver.")
                continue
            
            while True:
                try:
                    devolver_ticket = int(input("\nIngrese la cantidad de entradas que desea devolver: "))
                    if devolver_ticket > 0:
                        if devolver_ticket <= entradas_compradas:
                            entradas_disponibles += devolver_ticket
                            entradas_compradas -= devolver_ticket
                            entradas_devueltas += devolver_ticket
                            print(f"\n{devolver_ticket} entradas devueltas con exito.")
                            input("\nPresione [ENTER] para volver.")
                            clear_screen()
                            break
                        else:
                            print(f"\nError: No puedes devolver mas entradas de las que ha comprado ({entradas_compradas})")
                    else:
                        print("\nError: La cantidad no puede ser negativa o cero")
                        input("\nPresione [ENTER] para volver al menú.")
                        break
                except ValueError:
                    print("\nError: Ingrese un numero entero positivo")
        elif opc_menu == 4:
            print("\nGracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
            break
        else:
            print("\nIngrese una opcion valida.")
    except ValueError:
        print("\nError: El sistema solo considera numeros enteros.")