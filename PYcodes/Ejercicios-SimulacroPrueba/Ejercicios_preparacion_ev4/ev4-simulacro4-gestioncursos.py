import os

cursos_list_pregen = [
        {'nombre': 'python', 'cupos': 15, 'precio': 29.99, 'disponibilidad': True},
        {'nombre': 'javascript', 'cupos': 0, 'precio': 19.99, 'disponibilidad': False},
        {'nombre': 'diseño web', 'cupos': 8, 'precio': 45.00, 'disponibilidad': True},
        {'nombre': 'bases de datos', 'cupos': 25, 'precio': 35.50, 'disponibilidad': True},
        {'nombre': 'excel avanzado', 'cupos': 0, 'precio': 12.00, 'disponibilidad': False}
    ]

# Borrar pantalla
def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Menu con input
def menu():
    while True:
        print(f'''
        ===   MENÚ  ===
        ===============
        1. Agregar curso
        2. Buscar curso
        3. Eliminar curso
        4. Actualizar disponibilidad
        5. Mostrar cursos
        6. Salir
''')
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion in [1,2,3,4,5,6]:
                return opcion
            else:   
                print("Error: Opcion ingresada no existe.")
        except ValueError:
            print("Error: Ingrese un numero entero")

# Validar nombre
def validar_nombre(nombre):
    return nombre.strip() != ""

# Validar cupos
def validar_cupos(cupos):
    return cupos >= 0

# Validar precio
def validar_precio(precio):
    return precio > 0

# Agregar curso
def agregar_curso(cursos_list):
    nom_curso = input("Ingrese el nombre del curso a agregar: ").strip().lower()
    try:
        cupos = int(input("Ingrese la cantidad de cupos: "))
        precio = float(input("Ingrese el precio del curso: "))
    except ValueError:
        print("Error: datos ingresados incorrectos")
        return
        
    if validar_cupos(cupos) and validar_nombre(nom_curso) and validar_precio(precio):
        curso = {
            'nombre':nom_curso,
            'cupos':cupos,
            'precio':precio,
            'disponibilidad':False
        }
        cursos_list.append(curso)
        print("Curso registrado con exito!")

# Buscar curso
def buscar_curso(cursos_list, nom_curso):
    for curso in cursos_list:
        if curso['nombre'] == nom_curso:
            print("Curso encontrado")
            return curso
    return -1

# Mostrar datos de curso
def mostrar_datos_curso(nom_curso):
    print(f'''
Curso: {nom_curso['nombre']}
Cupos: {nom_curso['cupos']}
Precio: ${nom_curso['precio']}
''')
    if nom_curso['disponibilidad']:
        print("\nEstado: Diponible")
    else:
        print("\nEstado: No disponible")

# Ejecutar busqueda de curso
def busqueda_curso_exe(cursos_list):
    nom_curso = input("Ingrese el nombre del curso: ").strip().lower()
    curso_encontrado = buscar_curso(cursos_list, nom_curso)
    if curso_encontrado != -1:
        mostrar_datos_curso(curso_encontrado)
    else:
        print("\nCurso no encontrado")

# Eliminar curso
def eliminar_curso(cursos_list):
    curso_a_borrar = input("Ingrese el nombre del curso que desea eliminar: ").strip().lower()
    for curso in cursos_list:
        if curso['nombre'] == curso_a_borrar:
            cursos_list.remove(curso)

# Actualizar diponibilidad
def actualizar_disponibilidad(cursos_list):
    for curso in cursos_list:
        if curso['cupos'] > 0:
            curso['disponibilidad'] = True
        else:
            curso['disponibilidad'] = False

# Mostrar los cursos
def mostrar_cursos(cursos_list):
    if len(cursos_list) == 0:
        print("No se han registrado cursos.")
    else:
        for curso in cursos_list:
            print(f'''
        Nombre: {curso['nombre']}
        Cupos: {curso['cupos']}
        Precio: $ {curso['precio']}
    ''')
            if curso['disponibilidad']:
                print("Estado: Disponible")
            else:
                print("Estado: No diponible")

# Director
def main():
    clean_screen()
    cursos_list = []
    cursos_list.extend(cursos_list_pregen)
    print("\nCursos precargados con exito!")
    input("\n Presiona [ENTER] para comenzar...")
    while True:
        opcion = menu()
        if opcion == 1:
            clean_screen()
            agregar_curso(cursos_list)
        elif opcion == 2:
            clean_screen()
            busqueda_curso_exe(cursos_list)
        elif opcion == 3:
            clean_screen()
            eliminar_curso(cursos_list)
        elif opcion == 4:
            clean_screen()
            actualizar_disponibilidad(cursos_list)
        elif opcion == 5:
            clean_screen()
            mostrar_cursos(cursos_list)
        elif opcion == 6:
            print("\nSaliendo del programa.")
            break
        input("\nPresione [ENTER] para continuar")

# ---------> Programa <---------
main()