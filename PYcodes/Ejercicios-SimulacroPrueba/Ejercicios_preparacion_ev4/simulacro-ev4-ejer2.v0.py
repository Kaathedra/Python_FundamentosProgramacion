# ============================================================
# FPY1101 - Ejercicio 2: Sistema de gestión de estudiantes
# Tema: Listas, diccionarios, funciones, validaciones y menú
# ============================================================

# Cada estudiante debe almacenarse como un diccionario con:
# "nombre"    -> texto no vacío
# "edad"      -> entero mayor o igual que 18
# "promedio"  -> decimal entre 1.0 y 7.0
# "aprobado"  -> booleano, inicia en False

# ------------------------------------------------------------
# Función: cargar_estudiantes_inicial
# Objetivo: Cargar 10 alumnos por defecto para facilitar pruebas.
# ------------------------------------------------------------
def cargar_estudiantes_inicial(estudiantes):
    inventario = [
        {"nombre": "Ana Pérez", "edad": 20, "promedio": 5.8, "aprobado": False},
        {"nombre": "Carlos Silva", "edad": 18, "promedio": 3.5, "aprobado": False},
        {"nombre": "María Pardo", "edad": 22, "promedio": 4.0, "aprobado": False},
        {"nombre": "Juan Reyes", "edad": 19, "promedio": 6.2, "aprobado": False},
        {"nombre": "Sofía Díaz", "edad": 21, "promedio": 3.9, "aprobado": False},
        {"nombre": "Diego Torres", "edad": 25, "promedio": 5.5, "aprobado": False},
        {"nombre": "Laura Muñoz", "edad": 20, "promedio": 2.8, "aprobado": False},
        {"nombre": "Pedro Soto", "edad": 23, "promedio": 4.2, "aprobado": False},
        {"nombre": "Elena Castro", "edad": 19, "promedio": 6.7, "aprobado": False},
        {"nombre": "Luis Venegas", "edad": 18, "promedio": 3.1, "aprobado": False}
    ]
    estudiantes.extend(inventario)
    print("📢 Inventario inicial de 10 estudiantes cargado con éxito.")


# ------------------------------------------------------------
# Función: mostrar_menu
# Objetivo: Mostrar las opciones principales del sistema.
# ------------------------------------------------------------
def mostrar_menu():
    print('''
    ====== MENU PRINCIPAL ======
      1. Agregar estudiante
      2. Buscar estudiante
      3. Eliminar estudiante
      4. Actualizar estado de aprobación
      5. Mostrar estudiantes
      6. Salir
    ===========================''')


# ------------------------------------------------------------
# Función: leer_opcion
# Objetivo: Solicitar y validar la opción elegida por el usuario.
# Debe validar que sea entero y esté entre 1 y 6.
# ------------------------------------------------------------
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: opción debe estar entre 1 y 6.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")


# ------------------------------------------------------------
# Funciones de Validación (Para ser completadas por el estudiante)
# ------------------------------------------------------------
def validar_nombre(nombre):
    # Retorna True si es válido, False si es inválido.
    return nombre.strip() != ""

def validar_edad(edad):
    # Retorna True si es válida, False si es inválida.
    return edad >= 18

def validar_promedio(promedio):
    # Retorna True si es válido, False si es inválido.
    return 1.0 <= promedio <= 7.0


# ------------------------------------------------------------
# Función: agregar_estudiante
# Objetivo: Solicitar, validar e incorporar un nuevo alumno.
# (Para ser completada por el estudiante)
# ------------------------------------------------------------
def agregar_estudiante(estudiantes):
    nombre = input("Ingrese nombre del estudiante: ")
    
    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío.")
        return
    try:
        edad = int(input("Ingrese edad: "))
        promedio = float(input("Ingrese promedio (1.0 - 7.0): "))
    except ValueError:
        print("Error: valores no permitidos.")
        return
    if validar_edad(edad) and validar_promedio(promedio):
        estudiante = {
            'nombre': nombre.strip(),
            'edad': edad,
            'promedio': promedio,
            'aprobado': False
        }
        estudiantes.append(estudiante)
    else:
        print("Error: Valores ingresados no validos.")


# ------------------------------------------------------------
# Función: buscar_estudiante
# Objetivo: Buscar un alumno por su nombre.
# Retorna: La posición (índice) o -1 si no existe.
# (Para ser completada por el estudiante)
# ------------------------------------------------------------
def buscar_estudiante(estudiantes, nombre_buscado):
    for i in range(len(estudiantes)):
        if estudiantes[i]["nombre"].lower() == nombre_buscado.strip().lower():
            return i
    return -1


# ------------------------------------------------------------
# Función: mostrar_datos_estudiante
# Objetivo: Desplegar de forma ordenada los datos de un alumno.
# ------------------------------------------------------------
def mostrar_datos_estudiante(estudiante):
    print(f"Nombre   : {estudiante['nombre']}")
    print(f"Edad     : {estudiante['edad']} años")
    print(f"Promedio : {estudiante['promedio']}")
    
    if estudiante['aprobado']:
        print("Estado   : APROBADO")
    else:
        print("Estado   : REPROBADO")
    print("-" * 35)


# ------------------------------------------------------------
# Función: ejecutar_busqueda
# Objetivo: Interfaz de consola para la opción de buscar.
# (Para ser completada por el estudiante)
# ------------------------------------------------------------
def ejecutar_busqueda(estudiantes):
    nombre = input("Ingrese el nombre del estudiante a buscar: ").strip().lower()
    posicion = buscar_estudiante(estudiantes, nombre)
    
    if posicion != -1:
        print("== Estudiante encontrado ==")
        mostrar_datos_estudiante(estudiantes[posicion])
    else:
        print("El estudiante buscado no se ha encontrado.")


# ------------------------------------------------------------
# Función: eliminar_estudiante
# Objetivo: Buscar y remover a un estudiante del registro.
# (Para ser completada por el estudiante)
# ------------------------------------------------------------
def eliminar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip().lower()
    posicion = buscar_estudiante(estudiantes, nombre)
    
    if posicion != -1:
        eliminado = estudiantes.pop(posicion)
        print("Estudiante aliminad con exito.")
    else:
        print("Error: Estudiante no encontrado")

# ------------------------------------------------------------
# Función: actualizar_aprobacion
# Objetivo: Evaluar y modificar el campo "aprobado" (>= 4.0).
# (Para ser completada por el estudiante)
# ------------------------------------------------------------
def actualizar_aprobacion(estudiantes):
    for i in range(len(estudiantes)):
        if estudiantes[i]['promedio'] >= 4.0:
            estudiantes[i]['aprobado'] = True
        else:
            estudiantes[i]['aprobado'] = False


# ------------------------------------------------------------
# Función: mostrar_estudiantes
# Objetivo: Desplegar el listado completo actualizado.
# ------------------------------------------------------------
def mostrar_estudiantes(estudiantes):
    # Se exige que antes de mostrar se sincronice el estado de aprobación
    actualizar_aprobacion(estudiantes)
    
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return
        
    print("\n=== LISTA DE ESTUDIANTES ===")
    for est in estudiantes:
        mostrar_datos_estudiante(est)
    print("===== FIN LISTADO =====")


# ------------------------------------------------------------
# Función principal: main
# Objetivo: Orquestar el ciclo de vida de la aplicación.
# ------------------------------------------------------------
def main():
    estudiantes = [] # Se inicializa la lista vacía
    
    # Carga automática del inventario para pruebas rápidas
    cargar_estudiantes_inicial(estudiantes)
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_estudiante(estudiantes)
        elif opcion == 2:
            ejecutar_busqueda(estudiantes)
        elif opcion == 3:
            eliminar_estudiante(estudiantes)
        elif opcion == 4:
            actualizar_aprobacion(estudiantes)
            print("🔄 Estados de aprobación recalculados de forma global.")
        elif opcion == 5:
            mostrar_estudiantes(estudiantes)
        elif opcion == 6:
            print("Saliendo del sistema de gestión... ¡Hasta luego!")
            break


# ------------------------------------------------------------
# Inicio del programa
# ------------------------------------------------------------
main()