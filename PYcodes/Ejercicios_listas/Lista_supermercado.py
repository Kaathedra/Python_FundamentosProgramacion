lista_productos = []

lista_precios = []

lista_cantidades = []

lista_totales = []

while True:
    try:
        ingresar_producto = int(input("Presione 1 para ingresar un producto (para salir 0):"))
    except:
        print("Error: Ingrese un número")
        continue
    if ingresar_producto == 1:
        nom_producto = input("Ingresa el producto a registrar: ")
        lista_productos.append(nom_producto)
    elif ingresar_producto == 0:
        break
    else:
        print("Error: Opcion no valida.")

for i in range(len(lista_productos)):
    while True:
        try:
            precio_producto = int(input(f"Ingresa el precio unitario de '{lista_productos[i]}': "))
            if precio_producto == 0:
                print("Presionaste 0. Terminando compra.")
                exit()
            elif 100 <= precio_producto <= 100000:
                lista_precios.append(precio_producto)
                break
            else:
                print("Valor fuera del rango [100 - 100.000]")
        except:
            print("Error: Ingresa un valor entero.")
    while True:
        try:
            cant_producto = int(input(f"Ingrese la cantidad de '{lista_productos[i]}' a comprar: "))
            if cant_producto > 0:
                lista_cantidades.append(cant_producto)
                totales = lista_cantidades[i] * lista_precios[i]
                lista_totales.append(totales)
                break
            else:
                print("Error: La cantidad no puede ser negativa o cero")
        except:
            print("Error: Ingresa un numero entero positivo")

# Falta terminar BOLETA y verificar si aplica descuento #

