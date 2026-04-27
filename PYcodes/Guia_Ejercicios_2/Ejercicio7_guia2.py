for i in range (1,6):
    print(f"Trabajador N°{i}")
    sueldo_base = int(input("Ingrese su sueldo base: "))
    
    if sueldo_base < 500000:
        bono = sueldo_base * 0.10
        sueldo_final = sueldo_base + bono
        print(f"Se aplica un bono del 10%: ${int(bono)}")

    else:
        sueldo_final = sueldo_base
        print("No aplica bono.")
    print(f"Sueldo final a pagar: ${int(sueldo_final)}")