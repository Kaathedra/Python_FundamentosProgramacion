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
            print("El codigo de identificacion debe ser de al menos 6 caracteres, todos en mayusculas y no contener espacios.")
            net_id = input(f"Ingrese un codigo de identificacion de red para el operador {i + 1}: ").strip()
            if len(net_id) >= 6 and " " not in net_id and net_id.isupper():
                break
            else:
                print("Error: Codigo invalido, respete los requerimientos.")
    while True:
        try:
            credential = int(input(f"Ingrese el nivel de credencial del operador {i + 1}: "))
            if credential > 3 and credential <= 5:
                agente_elite.append(net_id)
                break
            elif credential >= 1 and credential <= 3:
                analista_soporte.append(net_id)
                break
            else:
                print("Fallo de autenticación: Ingrese un numero dentro del rango (1-5)")
        except ValueError:
            print("Error: Ingrese un numero entero valido.")

print(f"Finalizado el registro: ¡El complejo cuenta con {len(agente_elite)} Agentes de Élite y {len(analista_soporte)} Analistas de Soporte!¡Corta fuegos activos!")