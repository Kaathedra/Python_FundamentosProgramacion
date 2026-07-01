import os

talleres_presave = [
    {
        'nombre': 'introduccion a python',
        'codigo': 'PY-01',
        'precio': 45000.0,
        'cupos': 15,            # Al actualizar, este debería quedar DISPONIBLE
        'disponible': False
    },
    {
        'nombre': 'diseño de algoritmos',
        'codigo': 'AL-02',
        'precio': 60000.0,
        'cupos': 0,             # Al actualizar, este debería quedar SIN CUPOS
        'disponible': False
    },
    {
        'nombre': 'base de datos sql',
        'codigo': 'SQL-03',
        'precio': 55000.0,
        'cupos': 5,             # Al actualizar, este debería quedar DISPONIBLE
        'disponible': False
    }
]

# Borrar pantalla
def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Menú
def menu():
    print('''
========= MENÚ PRINCIPAL =========
    1. Agregar taller
    2. Buscar taller
    3. Eliminar taller
    4. Actualizar disponibilidad
    5. Mostrar talleres
    6. Salir
===================================
''')

# Leer opcion
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion in [1,2,3,4,5,6]:
                return opcion
            else:
                print("Error: Opcion ingresada no existe.")
        except ValueError:
            print("Error: Ingrese un numero entero.")

# Validar Codigo
def validar_codigo(codigo):
    return codigo.strip() != ""

# Validar Nombre
def validar_nombre(nombre):
    return nombre.strip() != ""

# Validar Cupos
def validar_cupos(cupos):
    return cupos >= 0

# Validar precios
def validar_precios(precio):
    return precio > 0

# Ingresar Taller
def ingresar_taller(talleres):
    nom_taller = input("Ingresa el nombre del taller: ").strip().lower()
    codigo = input("Ingrese el codigo del taller: ").strip().upper()
    try:
        precio = float(input("Ingrese el precio del taller: $"))
        cupos = int(input("Ingrese los cupos del taller: "))
    except ValueError:
        print("Datos ingresados no validos.")
        return
    if validar_codigo(codigo) and validar_cupos(cupos) and validar_nombre(nom_taller) and validar_precios(precio):
        taller = {
            'nombre':nom_taller,
            'codigo':codigo,
            'precio':precio,
            'cupos':cupos,
            'disponible':False
        }
        talleres.append(taller)
        print("Taller ingresado con éxito.")

# Buscar taller
def buscar_taller(talleres, codigo_buscado):
    for taller in talleres:
        if taller['codigo'] == codigo_buscado:
            print("Taller encontrado.")
            return taller
    return -1

# Mostrar datos taller
def mostrar_taller(codigo_buscado):
    print("="*60)
    print(f'''
Taller: {codigo_buscado['nombre']}

Codigo: {codigo_buscado['codigo']}

Precio: $ {codigo_buscado['precio']}

Cupos: {codigo_buscado['cupos']}
''')
    if codigo_buscado['disponible']:
        print("Estado: DISPONIBLE")
    else:
        print("Estado: SIN CUPOS")
    print("="*60)

# Ejecutar busqueda
def busqueda_exe(talleres):
    codigo_buscado = input("Ingrese el codigo del taller: ").upper().strip()
    taller_encontrado = buscar_taller(talleres,codigo_buscado)
    if taller_encontrado != -1:
        mostrar_taller(taller_encontrado)
    else:
        print("\nTaller no encontrado")

# Eliminar taller
def eliminar_taller(talleres):
    if len(talleres) == 0:
        print(f"{"NO HAY TALLERES REGISTRADOS":^50}")
        return
    else:
        codigo_buscado = input("Ingresa el codigo del taller a eliminar: ").upper().strip()
        taller_encontrado = buscar_taller(talleres, codigo_buscado)
        if taller_encontrado != -1:
            talleres.remove(taller_encontrado)
            print("\nTaller eliminado con exito.")
        else:
            print("\nTaller no encontrado")

# Actualizar disponibilidad
def actualizar_dispo(talleres):
    for taller in talleres:
        if taller['cupos'] > 0:
            taller['disponible'] = True
        else:
            taller['disponible'] = False
    print("Disponibilidad actualizada con exito")

# Mostrar talleres
def mostrar_talleres(talleres):
    if len(talleres) == 0:
        print(f"{"NO HAY TALLERES REGISTRADOS":^50}")
        return
    for taller in talleres:
        print("="*60)
        print(f'''
Nombre: {taller['nombre']}
Codigo: {taller['codigo']}
Precio: ${taller['precio']}
Cupos: {taller['cupos']}
''')
        if taller['disponible']:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN CUPOS")
    print(f"{"="*15}{"\n===== FIN DE LA LISTA ====":^20}{"="*15}")

# Orquestador
def main():
    talleres = []
    print("Existe una lista pregenerada. Desea cargarla?")
    carga = input("S/N: ").upper().strip()
    if carga == "S":
        talleres.extend(talleres_presave)
        clean_screen()
        print("Talleres precargados con exito!")
    else:
        pass
    input("\nPreiona [ENTER] para comenzar.")
    while True:
        clean_screen()
        menu()
        opcion = leer_opcion()
        if opcion == 1:
            clean_screen()
            ingresar_taller(talleres)
        elif opcion == 2:
            clean_screen()
            busqueda_exe(talleres)
        elif opcion == 3:
            clean_screen()
            eliminar_taller(talleres)
        elif opcion == 4:
            clean_screen()
            actualizar_dispo(talleres)
        elif opcion == 5:
            clean_screen()
            mostrar_talleres(talleres)
        elif opcion == 6:
            print("\nSaliendo del programa.")
            break
        input("\nPresiona [ENTER] para continuar")

# INICIO DEL PROGRAMA
main()