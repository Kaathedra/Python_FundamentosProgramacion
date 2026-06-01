stock = 50

sacos_despachados = 0

menu = '''
*** CONTROL DE BODEGA ***
1. Despachar sacos (Venta)
2. Mostrar stock actual
3. Mostrar cuantos sacos se han despachado en total
4. Salir
'''

while True:
    print(menu)
    try:
        opc_menu = int(input("Ingrese una opcion: "))
    except:
        print("Error: Ingrese un numero entero valido (1-4)")
        continue
    
    if opc_menu == 1:
        while True:
            try:
                saco_sale = int(input("Ingrese la cantidad de sacos a despachar: "))
            except:
                print("Error: Ingrese un numero entero positivo.")
                continue
            if 0 < saco_sale <= stock:
                print(f"Se despacharon con exito {saco_sale} sacos.")
                sacos_despachados += saco_sale
                stock -= saco_sale
                break
            else:
                print("Error: Has ingresado un numero negativo o no hay suficiente stock")
    elif opc_menu == 2:
        print(f"Stock actual: {stock} unidades.")
    elif opc_menu == 3:
        print(f"Se han despachado {sacos_despachados} sacos.")
    elif opc_menu == 4:
        print("Saliendo del menu...")
        break
    else:
        print("Opcion ingresada no valida.")