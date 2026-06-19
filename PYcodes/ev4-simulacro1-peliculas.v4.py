# ============================================================
# FPY1101 - ev4 Simulacro 1
# Ejercicio: Sistema de gestión de películas
# Tema: Listas, diccionarios, funciones, validaciones y menú
# ============================================================

# Cada película debe almacenarse como un diccionario con:
# "titulo"        -> texto no vacío
# "duracion"      -> entero mayor que 0
# "calificacion" -> decimal entre 1.0 y 5.0
# "recomendada"  -> booleano, inicia en False

# La lista principal debe almacenar todos los diccionarios
# de películas durante la ejecución del programa.


# ------------------------------------------------------------
# Función: cargar_inventario_inicial
# Objetivo:
# Cargar 10 películas por defecto para facilitar las pruebas.
# ------------------------------------------------------------
def cargar_inventario_inicial(peliculas):
    inventario = [
        {"titulo": "Inception", "duracion": 148, "calificacion": 4.8, "recomendada": False},
        {"titulo": "The Matrix", "duracion": 136, "calificacion": 4.7, "recomendada": False},
        {"titulo": "Interstellar", "duracion": 169, "calificacion": 4.6, "recomendada": False},
        {"titulo": "The Godfather", "duracion": 175, "calificacion": 4.9, "recomendada": False},
        {"titulo": "Pulp Fiction", "duracion": 154, "calificacion": 4.5, "recomendada": False},
        {"titulo": "Avatar", "duracion": 162, "calificacion": 3.9, "recomendada": False},
        {"titulo": "The Avengers", "duracion": 143, "calificacion": 4.1, "recomendada": False},
        {"titulo": "Gladiator", "duracion": 155, "calificacion": 4.3, "recomendada": False},
        {"titulo": "Shrek", "duracion": 90, "calificacion": 3.8, "recomendada": False},
        {"titulo": "Finding Nemo", "duracion": 100, "calificacion": 3.7, "recomendada": False}
    ]
    # Se extiende la lista principal con el inventario predefinido
    peliculas.extend(inventario)
    print("📢 Inventario inicial de 10 películas cargado con éxito.")

# ------------------------------------------------------------
# Función: mostrar_menu
# Objetivo:
# Mostrar las opciones del menú principal.
#
# No recibe parámetros.
# No retorna valores.
# ------------------------------------------------------------
def mostrar_menu():
    print('''
    ====== MENU PRICIPAL ======
      1. Agregar película
      2. Buscar película
      3. Eliminar película
      4. Actualizar recomendación
      5. Mostrar películas
      6. Salir
    ===========================''')


# ------------------------------------------------------------
# Función: leer_opcion
# Objetivo:
# Solicitar al usuario una opción del menú.
#
# Debe validar:
# - Que el dato ingresado sea un número entero.
# - Que esté entre 1 y 6.
#
# Retorna:
# - La opción validada.
# ------------------------------------------------------------
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Error: opcion debe estar entre 1 y 6.")
        except ValueError:
            print("Error: Debe ingresar un numero entero")

# ------------------------------------------------------------
# Función: validar_titulo
# Objetivo:
# Validar que el título no esté vacío ni tenga solo espacios.
#
# Recibe:
# - titulo
#
# Retorna:
# - True si es válido.
# - False si es inválido.
# ------------------------------------------------------------
def validar_titulo(titulo):
    return titulo.strip() != ""

# ------------------------------------------------------------
# Función: validar_duracion
# Objetivo:
# Validar que la duración sea mayor que 0.
#
# Recibe:
# - duracion
#
# Retorna:
# - True si es válida.
# - False si es inválida.
# ------------------------------------------------------------
def validar_duracion(duracion):
    return duracion > 0


# ------------------------------------------------------------
# Función: validar_calificacion
# Objetivo:
# Validar que la calificación esté entre 1.0 y 5.0.
#
# Recibe:
# - calificacion
#
# Retorna:
# - True si es válida.
# - False si es inválida.
# ------------------------------------------------------------
def validar_calificacion(calificacion):
    return calificacion >= 1.0 and calificacion <= 5.0


# ------------------------------------------------------------
# Función: agregar_pelicula
# Objetivo:
# Solicitar los datos de una película, validarlos y agregarla
# a la lista solo si todos los datos son correctos.
#
# Debe solicitar:
# - título
# - duración
# - calificación
#
# Debe crear un diccionario con las claves:
# - "titulo"
# - "duracion"
# - "calificacion"
# - "recomendada"
#
# La clave "recomendada" debe iniciar siempre en False.
#
# Recibe:
# - peliculas: lista donde se almacenan las películas.
#
# No retorna valores.
# ------------------------------------------------------------
def agregar_pelicula(peliculas):
    titulo = input("Ingrese titulo de la pelicula: ")
    
    if not validar_titulo(titulo):
        print("⚠️ Error: Título no puede estar vacío")
        return
    
    try:
        duracion = int(input("Duración en minutos: "))
    except ValueError:
        print("⚠️ Error: duración debe ser número entero")
        return
    
    if not validar_duracion(duracion):
        print("⚠️ Error: duración debe ser mayor que 0")
        
    try:
        calificacion = float(input("Calificación entre 1.0 y 5.0: "))
    except ValueError:
        print("⚠️ Error: calificacion debe ser decimal")
        return
    
    if not validar_calificacion(calificacion):
        print("⚠️ Error: calificación debe estar entre 1.0 y 5.0")
        return
    
    # Se crea el diccionario con las claves
    pelicula = {
        "titulo"        : titulo.strip(),
        "duracion"      : duracion,
        "calificacion"  : calificacion,
        "recomendada"   : False
    }
    
    # Se agrega a la lista
    peliculas.append(pelicula)
    print("Pelicula agregada correctamente")
    
    print(peliculas)

# ------------------------------------------------------------
# Función: buscar_pelicula
# Objetivo:
# Buscar una película por su título.
#
# Recibe:
# - peliculas: lista de películas.
# - titulo_buscado: título que se desea buscar.
#
# Retorna:
# - La posición de la película si existe.
# - -1 si no existe.
# ------------------------------------------------------------
def buscar_pelicula(peliculas, titulo_buscado):
    pass


# ------------------------------------------------------------
# Función: mostrar_datos_pelicula
# Objetivo:
# Mostrar los datos de una película específica.
#
# Recibe:
# - pelicula: diccionario con los datos de una película.
#
# No retorna valores.
# ------------------------------------------------------------
def mostrar_datos_pelicula(pelicula):
    print(f"Título      : {pelicula['titulo']}")
    print(f"Duración    : {pelicula['duracion']}")
    print(f"Calificación: {pelicula['calificacion']}")
    
    if pelicula['recomendada']:
        print("Estado: RECOMENDADA")
    else:
        print("Estado: NO RECOMENDADA")
    print("-" * 30)


# ------------------------------------------------------------
# Función: ejecutar_busqueda
# Objetivo:
# Solicitar al usuario el título de una película,
# llamar a la función buscar_pelicula y mostrar el resultado.
#
# Recibe:
# - peliculas: lista de películas.
#
# No retorna valores.
# ------------------------------------------------------------
def ejecutar_busqueda(peliculas):
    pass


# ------------------------------------------------------------
# Función: eliminar_pelicula
# Objetivo:
# Eliminar una película usando la función de búsqueda.
#
# Debe:
# - Solicitar el título de la película a eliminar.
# - Llamar a buscar_pelicula.
# - Si existe, eliminarla usando su posición.
# - Si no existe, mostrar un mensaje.
#
# Recibe:
# - peliculas: lista de películas.
#
# No retorna valores.
# ------------------------------------------------------------
def eliminar_pelicula(peliculas):
    pass


# ------------------------------------------------------------
# Función: actualizar_recomendacion
# Objetivo:
# Actualizar el campo "recomendada" de todas las películas.
#
# Regla:
# - Si la calificación es mayor o igual a 4.0,
#   "recomendada" debe ser True.
# - Si la calificación es menor a 4.0,
#   "recomendada" debe ser False.
#
# Recibe:
# - peliculas: lista de películas.
#
# No retorna valores.
# ------------------------------------------------------------
def actualizar_recomendacion(peliculas):
    pass


# ------------------------------------------------------------
# Función: mostrar_peliculas
# Objetivo:
# Mostrar todas las películas registradas.
#
# Antes de mostrar, debe llamar a actualizar_recomendacion.
#
# Recibe:
# - peliculas: lista de películas.
#
# No retorna valores.
# ------------------------------------------------------------
def mostrar_peliculas(peliculas):
    actualizar_recomendacion(peliculas)
    
    if len(peliculas) == 0:
        print("No hay peliculas registradas")
        return
    
    print("\n=== LISTA DE PELICULAS ===")
    for pelicula in peliculas:
        mostrar_datos_pelicula(pelicula)
    
    print("===== FIN LISTADO =====")
    


# ------------------------------------------------------------
# Función principal: main
# Objetivo:
# Controlar el funcionamiento general del programa.
#
# Debe:
# - Crear la lista vacía de películas.
# - Mantener activo el ciclo del menú.
# - Llamar a mostrar_menu y leer_opcion en cada vuelta.
# - Ejecutar la función correspondiente según la opción.
# - Finalizar cuando el usuario seleccione salir.
# ------------------------------------------------------------
def main():
    peliculas = [] # Se inicializa correctamente vacía
    
    # Llamada automática al cargar el programa
    cargar_inventario_inicial(peliculas) 
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            agregar_pelicula(peliculas) 
        elif opcion == 2:
            ejecutar_busqueda(peliculas)
        elif opcion == 3:
            eliminar_pelicula(peliculas)
        elif opcion == 4:
            actualizar_recomendacion(peliculas)
            print("🔄 Recomendaciones actualizadas según su calificación actual.")
        elif opcion == 5:
            mostrar_peliculas(peliculas)
        elif opcion == 6:
            print("Saliendo del sistema...")
            break

# ------------------------------------------------------------
# Inicio del programa
# ------------------------------------------------------------
main()