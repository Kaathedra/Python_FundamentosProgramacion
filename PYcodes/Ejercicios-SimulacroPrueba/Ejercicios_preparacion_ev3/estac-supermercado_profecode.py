# Variables globales para control y estadísticas
total_recaudado = 0
cantidad_vehiculos = 0
total_minutos = 0
total_boletas = 0

menu = '''
  *** CONTROL DE ESTACIONAMIENTO SUPERMERCADO ***
1. Ingresar vehículo
2. Mostrar total de dinero recaudado
3. Mostrar cantidad de vehículos registrados
4. Mostrar promedio de permanencia en minutos
5. Mostrar promedio de valor de boletas registradas
6. Terminar programa'''

while True:
    print(menu)
    opcion = input("Elija opción: ")
    
    if opcion == "1":
        # 1. Validación de los minutos de permanencia
        while True:
            try:
                minutos = int(input("Ingrese minutos de permanencia: "))
                if minutos >= 0:
                    break
                else:
                    print("Error: Los minutos no pueden ser negativos.")
            except ValueError:
                print("Debe ingresar un número entero válido.")
                
        # 2. Validación del valor de la boleta del supermercado
        while True:
            try:
                boleta = int(input("Ingrese valor de la boleta del supermercado: "))
                if boleta >= 0:
                    break
                else:
                    print("Error: El valor de la boleta no puede ser negativo.")
            except ValueError:
                print("Debe ingresar un número entero válido.")
        
        # 3. Aplicación de las Reglas de Negocio para el cálculo del cobro
        cobro = 0
        if boleta > 200000:
            cobro = 0
        elif boleta > 30000:
            if minutos > 30:
                cobro = (minutos - 30) * 50
            else:
                cobro = 0
        else:
            cobro = minutos * 50
            
        # 4. Actualización de datos estadísticos
        total_recaudado += cobro
        cantidad_vehiculos += 1
        total_minutos += minutos
        total_boletas += boleta
        
        print(f"Vehículo registrado con éxito. Total a pagar: ${cobro}")
        
    elif opcion == "2":
        print(f"Total de dinero recaudado hasta el momento: ${total_recaudado}")
        
    elif opcion == "3":
        print(f"Cantidad de vehículos registrados: {cantidad_vehiculos}")
        
    elif opcion == "4":
        # Validación para evitar la división por cero si no hay vehículos
        if cantidad_vehiculos > 0:
            promedio_minutos = total_minutos / cantidad_vehiculos
            print(f"promedio de permanencia: {promedio_minutos:.1f} minutos.")
        else:
            print("Aún no se han registrado vehículos en el sistema.")
            
    elif opcion == "5":
        # Validación para evitar la división por cero si no hay boletas
        if cantidad_vehiculos > 0:
            promedio_boletas = total_boletas / cantidad_vehiculos
            print(f"promedio de valor de boletas registradas: ${promedio_boletas:.0f}")
        else:
            print("Aún no se han registrado boletas en el sistema.")
            
    elif opcion == "6":
        print("Fin del programa. Caja cerrada exitosamente.")
        break
        
    else:
        print("Debe ingresar una opción válida (1-6).")