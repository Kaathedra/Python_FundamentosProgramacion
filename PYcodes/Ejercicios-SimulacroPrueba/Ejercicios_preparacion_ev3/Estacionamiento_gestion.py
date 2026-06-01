vehiculo_registrado = 0
recaudado_total = 0

menu = ''' 
*** SISTEMA DE ESTACIONAMIENTO ***
1. Registrar ingreso de vehiculo
2. Mostra total de dinero recaudado
3. Mostrar cantidad de vehiculos registrados
4. Terminar programa
'''

while True:
    print(menu)
    try:
        opc_menu = int(input("Ingresa una opción: "))
    except ValueError:
        print("Error: Ingresa una opcion valida (1-4)")
        input("Presiona [ENTER] para volver al menú")
        continue
    if opc_menu == 1:
        while True:
            reg_vehiculo = input("El cobro por vehiculo es de $2500 clp. Desea proceder?(s/n): ").strip().lower()
            if reg_vehiculo == "s":
                vehiculo_registrado += 1
                recaudado_total += 2500
                print("vehiculo registrado con exito!")
                input("Presiona [ENTER] para volver al menú")
                break
            elif reg_vehiculo == "n":
                break
            else:
                print("Error: Ingresa una opcion valida (s/n)")
    elif opc_menu == 2:
        if recaudado_total == 0:
            print("No se han registrado vehiculos. No hay un monto recaudado.")
        else:
            print(f"Se ha recaudado un total de $ {recaudado_total} clp.")
        input("Presiona [ENTER] para volver al menú")
    elif opc_menu == 3:
        if vehiculo_registrado == 0:
            print("No se han registrado vehiculos.")
        else:
            print(f"Hay un total de {vehiculo_registrado} vehiculos regitrados.")
        input("Presiona [ENTER] para volver al menú")
    elif opc_menu == 4:
        print("Fin del programa. Sistema cerrado.")
        break
    else:
            print("Error: Esa opción no existe en el menú (Elige de 1 a 4).")
            input("Presiona [ENTER] para volver al menú")