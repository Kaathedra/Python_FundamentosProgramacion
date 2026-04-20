import os

totalTalca = 0
totalConce = 0
totalPtoMontt = 0


opcion = 0
while opcion != 3:
    print("===== VENTA DE PASAJES =====")
    print("1. Comprar pasajes")
    print("2. Ver resumen de ventas")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion (1-3): "))

    if opcion == 1:
        print("Seleccione el destino:")
        print("1. Talca ($10.000)")
        print("2. Concepción ($20.000)")
        print("3. Puerto Montt ($35.000)")
        destino = int(input("Ingrese destino (1-3): "))
        
        if destino == 1:
            nom_destino = "Talca"
            precio = 10000
            cantidad = int(input("Ingrese cantidad de pasajes a Talca: "))
            totalTalca = totalTalca + cantidad
            subtotal = precio * cantidad
            
        elif destino == 2:
            nom_destino = "Concepcion"
            precio = 20000
            cantidad = int(input("Ingrese cantidad de pasajes a Conce: "))
            totalConce = totalConce + cantidad
            subtotal = precio * cantidad
            
        elif destino == 3:
            nom_destino = "Puerto Montt"
            precio = 35000
            cantidad = int(input("cantidad de pasajes a Pto Montt: "))
            totalPtoMontt = totalPtoMontt + cantidad
            subtotal = precio * cantidad
            
        else:
            print("Destino invalido")
            
        has_dcto = str(input("Tiene tajeta de descueto?(s/n): ")).strip().lower()
        if has_dcto == "s":
            dcto = subtotal * 0.1
            TotalCompra = subtotal - dcto
        elif has_dcto == "n":
            TotalCompra = subtotal
        else:
            print("Error de Ingreso")
        
        print("="*5, "Boleta", "="*5)
        print(f"Destino: {nom_destino}")
        print(f"Cantidad de pasajes: {cantidad}")
        print(f"Subtotal: {subtotal}")
        
        # falta preguntar si tiene tarjeta descuento
        # calcular descuento
        # mostrar la boleta
        
    elif opcion == 2:
        print("==== RESUMEN DE VENTAS ====")    	    
        print("Pasajes a Talca: ", totalTalca)
        print("Pasajes a Concepción: ", totalConce)
        print("Pasajes a Puerto Montt: ", totalPtoMontt)
        
    elif opcion == 3:
        print("saliendo")
    else:
        print("Opcion incorrecta, reingrese")

    input("\n\nEnter para continuar al menu")
    os.system("cls")
# fin while opcion
print("\nGracias por utilizar programa")
input("\n\nPresione Enter para terminar")