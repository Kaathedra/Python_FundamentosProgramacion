agente_elite = []
analista_soporte = []

while True:
    try:
        ingreso_operador = int(input("Ingrese la cantidad de operadores a registrar: "))
        if ingreso_operador > 0:
            break
        else:
            print("Error: La cantidad no puede ser 0 o un negativa.")
    except ValueError:
        print("Ingrese un numero entero valido")

for i in range(ingreso_operador):
    while True:
            net_id = input(f"Ingrese un codigo de identificacion de red para el operador {i + 1}: ").strip()
            if len(net_id) >= 6 and " " not in net_id and net_id.isupper():
                break
            else:
                print("Error: Codigo invalido, respete los requerimientos.")
    while True:
        try:
            credential = int(input(f"Ingrese el nivel de credencial del operador {i + 1}"))
            if credential > 3