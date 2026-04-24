import os

def borrar_screen():
    os.system("cls")

def pausa():
    input("\nPresiona Enter para continuar...")

def barra():
    print("="*25)
    return

saldo = 5000
while True:
    borrar_screen()
    print("===== ATM ======")
    print(" 1. Mostrar saldo \n 2. Girar dinero \n 3. Salir")
    try:
        opcion = (int(input("ingresa una opcion (1-3): ")))
        if opcion == 1:
            borrar_screen()
            barra()
            print(f"Tu saldo es de ${saldo:,}".replace(",","."))
            barra()
            pausa()
        elif opcion == 2:
            borrar_screen()
            barra()
            giro = int(input("Ingresa el monto que deseas girar: "))
            if giro > saldo:
                borrar_screen()
                barra()
                print("Fondos Insuficientes.")
            elif giro <= 0:
                borrar_screen()
                barra()
                print("El monto debe ser mayor a 0.")
                pausa()
            else:
                saldo -= giro
                borrar_screen()
                barra()
                print(f"Giro exitoso. Nuevo saldo: {saldo}")
                pausa()
        elif opcion == 3:
            borrar_screen()
            barra()
            print("Saliendo de cajero...")
            barra()
            break
        else:
            barra()
            print("Error de ingreso.")
            pausa()
    except ValueError:
        barra()
        print("Error. Ingresa una opcion válida.")
        pausa()