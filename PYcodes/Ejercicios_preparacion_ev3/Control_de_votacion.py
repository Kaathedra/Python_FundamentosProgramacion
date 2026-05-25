import os
def menu():
    print('''
    === MENU DE VOTACION ===
    1. Registrar votante
    2. Mostrar cantidad de votantes
    3. Mostrar edad del votante mas joven
    4. Terminar programa
''')

votante_list = []

def reg_votante():
    while True:
        try:
            edad = int(input("Ingrese la edad del votante: "))
            if 18 <= edad <= 100:
                print("Votante registrado con exito")
                votante_list.append(edad)
                break
            else:
                print("edad no permitida para votar")
        except ValueError:
            print("Ingrese un numero entero")

os.system("cls")

while True:
    menu()
    try:
        opcion_menu = int(input("Ingrese una opcion: "))
        if opcion_menu == 1:
            reg_votante()
        elif opcion_menu == 2:
            print(f"\nCantidad de votantes: {len(votante_list)}")
        elif opcion_menu == 3:
            if len(votante_list) > 0:
                print(f"\nVotante mas jóven: {min(votante_list)} años.")
            else:
                print("\nNo se han registrado votantes aun.")
        elif opcion_menu == 4:
            print("\nSaliendo del programa...")
            break
        else:
            print("\nError: Ingresa una numero valido (1-4)")
    except ValueError:
        print("\nIngresa una opcion valida (1-4)")