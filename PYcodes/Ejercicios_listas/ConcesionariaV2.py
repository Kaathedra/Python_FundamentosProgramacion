import os

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

autos_lista = []

# Funcion Menú con input interno #
def menu():
    print("="*50)
    print(f"{'MENÚ PRINCIPAL':^50}")
    print("="*50)
    print(''' 
    1. Agregar vehiculo
    2. Buscar vehivulo
    3. Eliminar vehiculo
    4. Actualizar disponibilidad
    5. Mostrar vehiculos
    0. Salir
''')
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion in [1,2,3,4,5,0]:
                return opcion
            else:
                print("\nError: La opcion ingresada no existe.")
        except ValueError:
            print("\nError: Ingrese un numero entero positivo como opcion.")

# Funcion para validar valores positivos #
def validar(precio):
    while True:
        try:
            valor = int(input(precio))
            if valor > 0:
                return valor
            else:
                print("\nError: Debe ser un número positivo")
        except ValueError:
            print("\nDato invalido: Ingrese un numero entero")

# Funcion para agregar vehiculo #
def agregar_vehiculo():
    while True:
        vehiculo_model = input("\nIngrese el modelo del vehiculo: ")
        if len(vehiculo_model) > 0:
            break

    vehiculo_price = validar("\nIngrese el precio del vehiculo: ")

    while True:
        vehiculo_anio = validar("\nIngrese el año del vehiculo: ")
        if 1900 < vehiculo_anio <= 2027:
            break
        print(f"Error: {vehiculo_anio} no es un año valido")
    autos_lista.append({"modelo":vehiculo_model,"precio":vehiculo_price,"año":vehiculo_anio,"disponible":False})
    print(f"\nVehiculo modelo: [{vehiculo_model}] registrado con exito.")

# Funcion para buscar vehiculos en base a modelos #
def vehiculo_search():
    print(f"{"Buscar vehiculo":^25}")
    busqueda = input("\nIngrese el modelo del vehiculo que desea buscar: ").strip().lower()
    if len(busqueda) > 0:
        encontrado = False
        for auto in autos_lista:
            disponibilidad = "Disponible" if auto["disponible"] else "No disponible"
            if auto["modelo"].lower() == busqueda:
                print("\nVehiculo encontrado")
                print(f'''
    Modelo: {auto["modelo"]}
    Año: {auto["año"]}
    Precio: {auto["precio"]}
    Disponibilidad: {disponibilidad}
    ''')
                encontrado = True
    if not encontrado:
        print("\nNo se encontró el vehiculo")

# Funcion para mostrar todos los vehiculos #
def vehiculos_show():
    if len(autos_lista) == 0:
        print("\nNo se han registrado vehiculos.")
        return
    else:
        print(f"{'Vehiculos en sistema':^50}")
        print("="*80)
        print(f"{'Modelo':<15}{'Año':>15}{'Precio':>15}{'Disponibilidad':>20}")
        print("="*80)
        for auto in autos_lista:
            disponibilidad = "Disponible" if auto["disponible"] else "No disponible"
            print(f"{auto["modelo"]:<15}{auto['año']:>15}${auto['precio']:>15}{disponibilidad:>20}")

# Funcion para eliminar vehiculos #

def vehiculo_delete():
    while True:
        eliminar = input("Ingrese el modelo del vehiculo a eliminar: ").strip().lower()
        encontrado = False
        for auto in autos_lista:
            if auto['modelo'].lower() == eliminar:
                autos_lista.remove(auto)
                print("\nEl vehiculo ha sido eliminado con exito")
                encontrado = True
                break
        if not encontrado:
            print("\nNo se ha encontrado el modelo ingresado")
        else:
            break

# Funcion para cambiar disponibilidad #
def dispo_change(autos_lista):
    for auto in autos_lista:
        if auto['año'] >= 2020:
            auto['disponible'] = True
        else:
            auto['disponible'] = False
    print("\nDisponibilidad actualizada con éxito.")

# Funcion para buscar vehiculos por modelo V2 #
def buscar_car_v2(lista, modelo_a_buscar):
    for i, auto in enumerate(lista):
        if auto['modelo'].lower() == modelo_a_buscar.lower():
            return i
    return -1

# Funcion para eliminar por modelo V2 #
def delete_car():
    posicion = buscar_car_v2() # <------ TERMINAR POR FAVAAAAARRRRRRR


# ------------------------> # PROGRAMA PRINCIPAL # <--------------------------

while True:
    clean_screen()
    opcion_menu = menu()
    if opcion_menu == 0:
        clean_screen()
        print("\nSaliendo del programa. Gracias por preferirnos.")
        exit()
    elif opcion_menu == 1:
        clean_screen()
        agregar_vehiculo()
    elif opcion_menu == 2:
        clean_screen()
        buscar_car_v2()
    elif opcion_menu == 3:
        clean_screen()
        vehiculo_delete()
    elif opcion_menu == 4:
        clean_screen()
        dispo_change(autos_lista)
    elif opcion_menu == 5:
        clean_screen()
        vehiculos_show()
    input("\nPresiona [ENTER] para continuar >")