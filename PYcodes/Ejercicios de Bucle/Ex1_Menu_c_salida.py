#  Crea un menú que se repita infinitamente (while True). Solo si el usuario elige la
# opción "Salir", el programa debe ejecutar un break.

def menu():
    print(''' 
    ==== MENU ====
    
    1. Opcion 1
    2. Opcion 2
    3. Salir
''')
    return input("Ingrese una opcion: ")


while True:
    opcion = menu()
    if opcion in ["1","2"]:
        continue
    elif opcion == "3":
        print("\nSaliendo...")
        break
    else:
        print("\nError: Ingresa una opcion correcta(1, 2 o 3)")