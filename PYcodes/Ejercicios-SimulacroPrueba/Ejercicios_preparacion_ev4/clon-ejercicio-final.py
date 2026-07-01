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
                continue
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
    for i in range(len(talleres)):
        if talleres[i]['codigo'] == codigo_buscado:
            return i
    return -1

# Mostrar datos taller
def mostrar_taller(talleres,i):
    taller = talleres[i]
    print("="*60)
    print(f'''
Taller: {taller['nombre']}

Codigo: {taller['codigo']}

Precio: $ {taller['precio']}

Cupos: {taller['cupos']}
''')
    if taller['disponible']:
        print("Estado: DISPONIBLE")
    else:
        print("Estado: SIN CUPOS")
    print("="*60)

# Ejecutar busqueda
def busqueda_exe(talleres):
    codigo_buscado = input("Ingrese el codigo del taller: ").upper().strip()
    i = buscar_taller(talleres,codigo_buscado)
    if i != -1:
        mostrar_taller(talleres, i)
    else:
        print("\nTaller no encontrado")

# Eliminar taller
def eliminar_taller(talleres):
    if len(talleres) == 0:
        print(f"{"NO HAY TALLERES REGISTRADOS":^50}")
        return

    codigo_taller = input("Ingresa el codigo del taller a eliminar: ").upper().strip()

    i = buscar_taller(talleres, codigo_taller)

    if i != -1:
        talleres.pop(i)
        print("Taller eliminado con exito")
    else:
        print("No se encontró el taller.")

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