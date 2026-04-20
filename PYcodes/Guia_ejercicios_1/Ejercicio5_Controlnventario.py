cant_actual = int(input("Ingresa la cantidad de productodisponible en bodega: "))
cant_min_req = int(input("Ingresa la cantidad minima requerida: "))
if cant_actual < cant_min_req:
    print("Alerta: Es necesario reponer stock")