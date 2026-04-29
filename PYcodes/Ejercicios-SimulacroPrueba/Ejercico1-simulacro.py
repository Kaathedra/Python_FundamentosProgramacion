while True:
    try:
        cant_mask = int(input("Ingresa cuantas macarillas deseas comprar: "))
        break
    except ValueError:
        print("Error. Ingresa un numero entero.")
    
subtotal = cant_mask * 500
print("\n 1. Misma comuna \n 2. Comuna cercana \n 3. Comuna Lejana")
valid_location = (1,2,3)
costos = {1:1000, 2:2000, 3:3000}

while True:
    try:
        location = int(input("\nIngresa la opcion que mas se asemeja a tu direccion de envio: "))
        
        if location in valid_location:
            costo_envio = costos[location]
            break
        else:
            print("Opcion ingresada no valida.")
    except ValueError:
        print("Error de ingreso. Ingresa solo números.(1, 2 o 3)")
total = subtotal + costo_envio
print("="*27)
print(f"""===== DETALLE DE LA COMPRA=====
    Cantidad de mascarillas: {cant_mask}
    Subtotal:                {subtotal}
    Costo de envío:          {costo_envio}
    ----------------------------------
    Total a pagar:           {total}
    """)