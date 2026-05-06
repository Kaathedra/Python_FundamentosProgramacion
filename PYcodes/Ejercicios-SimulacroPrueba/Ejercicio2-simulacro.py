unidad_moneda = {1:"Dolar",2:"UF",3:"UTM"}

print(''' =====CONVERSOR DE DIVISAS=====
        1. Dolar
        2. UF
        3. UTM''')
index = int(input("Ingresa la unidad que deseas  convertir: "))
if index in unidad_moneda:
    if index == 2:
        valor_unidad = float(input("Ingrese el valor actual de la UF: "))
    elif index == 1:
        valor_unidad = 850
    else:
        valor_unidad = 52500

    cantidad = float(input(f"Ingresa la cantidad de {unidad_moneda[index]} a convertir: "))

    valor_clp = cantidad * valor_unidad

    print(f'''
        =========Resumen========
        Referencia de moneda: {unidad_moneda[index]}
        Cantidad ingresada: {cantidad}
        Precio en CLP: {valor_clp}
''')
else:
    print("Error. Opcion no valida.")