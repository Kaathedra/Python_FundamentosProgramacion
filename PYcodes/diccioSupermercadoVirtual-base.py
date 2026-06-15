import os

# =====================================================================
# 1. BASE DE DATOS INICIAL (Diccionario de Productos)
# =====================================================================
# Estructura bidimensional nativa: { Código: { Nombre, Precio } }
productos = {
    "A01": {"nombre": "Arroz",  "precio": 1200},
    "A02": {"nombre": "Leche",  "precio": 950},
    "A03": {"nombre": "Huevos", "precio": 2800},
}

# =====================================================================
# 2. FUNCIONES MODULARES A COMPLETAR
# =====================================================================

def ver_productos():
    """
    REQUISITO 1: Debe mostrar en pantalla una tabla limpia y alineada con 
    todos los productos del diccionario global.
    Formato requerido por la pauta: Código - Nombre - Precio Unitario.
    """
    print(f"\n{'CATÁLOGO DE PRODUCTOS':^45}")
    print(f"{"\nCódigo":<15}{"Producto":^20}{"Precio":<15}")
    print("-" * 45)
    for codigo, info in productos.items():
        nombre = info["nombre"]
        precio = info["precio"]
        print(f"{codigo:<15}{nombre:^20}$ {precio:<15}")
    print("-" * 45)


def agregar_producto():
    """
    REQUISITO 2: Registrar un nuevo producto en el catálogo.
    - Solicitar código (Convertir a mayúsculas y limpiar espacios).
    - Validar que el código NO exista previamente en el diccionario.
    - Validar mediante try-except que el precio sea un entero positivo.
    """
    print("\n➕ --- REGISTRAR NUEVO PRODUCTO ---")
    while True:
            codigo = input("Ingrese un codigo para registrar nuevo producto: ").upper().replace(" ","")
            if codigo not in productos.items():
                while True:
                        nombre = input("Ingrese el nombre del producto: ").strip().lower()
                        if nombre not in productos["nombre"].items():
                            precio = float(input("Ingrese el precio del producto nuevo: $"))
                            productos[codigo] = {"nombre": nombre, "precio": precio}
                            break
    ## ----------------------> TERMINAR ESTA FUNCION. REVISAR SI ESTA BIEN. nO TE HAGAI WN TOMÁS <-----------------------
                        else: 
                            print("Error: Este producto ya existe en la base de datos.")
            else: 
                print("Error: Este codigo ya existe en la base de datos.")
    # TODO: Capturar y validar el código.
    # TODO: Capturar nombre y precio (añadir try-except para el precio).


def modificar_producto():
    """
    REQUISITO 3: Permitir alterar el nombre y/o precio de un producto existente.
    - Solicitar el código del producto.
    - Si existe, pedir nuevo nombre y precio (si se presiona ENTER sin escribir nada, 
      se deben mantener los datos originales).
    - Validar que el nuevo precio sea numérico entero y positivo.
    """
    print("\n🛠️ --- MODIFICAR PRODUCTO EXISTENTE ---")
    # TODO: Buscar el código del producto.
    # TODO: Implementar lógica de modificación condicional y validaciones de tipo.
    pass


def eliminar_producto():
    """
    REQUISITO 4: Remover permanentemente un producto de la base de datos.
    - Solicitar código.
    - Si existe en el diccionario, destruirlo usando la instrucción 'del'.
    - Si no existe, notificar el error explícitamente.
    """
    print("\n🗑️ --- ELIMINAR PRODUCTO ---")
    # TODO: Implementar la eliminación controlada mediante la palabra clave 'del'.
    pass


def procesar_compra():
    """
    REQUISITO 5: Módulo interactivo de adquisición y cálculo de boleta.
    - Instanciar un carrito de compras temporal (un diccionario vacío local).
    - Permitir agregar múltiples productos ingresando su código y cantidad hasta que escriba 'FIN'.
    - Emitir una boleta electrónica tabulada que calcule los subtotales y el neto total.
    - Preguntar si desea delivery. Si el neto supera $50,000, el delivery es GRATIS.
    - Si no supera los $50,000 y requiere despacho, sumar un cargo de $3,000.
    - Validar enérgicamente que la dirección de delivery no sea un campo vacío.
    """
    print("\n🛒 --- MÓDULO DE ADQUISICIÓN DE PRODUCTOS ---")
    carrito = {}  # Estructura sugerida para la sesión: { código: cantidad }
    
    # TODO: Crear ciclo 'while' para la selección de productos.
    # TODO: Renderizar boleta tabulada cruzando datos de 'carrito' con 'productos'.
    # TODO: Implementar lógica condicional de cobro de delivery y validación de dirección.
    pass


# =====================================================================
# 3. INTERFAZ Y CONTROL DE FLUJO PRINCIPAL (Orquestador)
# =====================================================================
while True:
    print("\n*********************************")
    print("  🖥️  MENÚ SUPERMERCADO VIRTUAL  ")
    print("*********************************")
    print("1. Ver productos disponibles")
    print("2. Agregar nuevo producto")
    print("3. Modificar producto existente")
    print("4. Eliminar producto")
    print("5. Comprar productos")
    print("6. Salir del sistema")
    print("*********************************")
    
    opcion = input("Seleccione una opción (1-6): ").strip()
    
    if opcion == "1":
        ver_productos()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        modificar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        procesar_compra()
    elif opcion == "6":
        print("\n👋 Saliendo del sistema informático... ¡Muchas gracias por su preferencia!")
        break
    else:
        print("⚠️ Opción inválida. Por favor, marque un dígito del 1 al 6.")
    
    input("\n⌨️ Presione ENTER para regresar al menú...")
    os.system("cls" if os.name == "nt" else "clear")