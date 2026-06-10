import os

# Diccionario principal
superheroes = {
    "ironman"   : {"fuerza": 9500,  "inteligencia": 10000},
    "spiderman" : {"fuerza": 7000,  "inteligencia": 9000},
    "hulk"      : {"fuerza": 15000, "inteligencia": 4000},
}

def mostrar_superheroes():
    print(f"\n{'Diccionario tabulado':^45}")
    print("-" * 45)
    print(f"{'NOMBRE':<15} {'FUERZA':^12} {'INTELIGENCIA':>12}")
    print("-" * 45)
    for nombre, atributos in superheroes.items():
        print(f"{nombre:<15} {atributos['fuerza']:^12} {atributos['inteligencia']:>12}")

def validar_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
        except:
            pass
        print("⚠️ Ingreso inválido, debe ser un número entero positivo.")

def agregar_superheroe():
    nombre = input("Nombre superheroe: ").lower()
    if nombre not in superheroes:
        fuerza = validar_positivo("Cantidad de fuerza: ")
        inteligencia = validar_positivo("Cantidad de inteligencia: ")
        superheroes[nombre] = {"fuerza": fuerza, "inteligencia": inteligencia}
        print(f"{nombre} agregado con éxito.")
    else:
        print(f"{nombre} ya existe.")

def buscar_superheroe():
    nombre = input("Nombre superheroe a buscar: ").lower()
    if nombre in superheroes:
        print(f"Encontrado: {superheroes[nombre]}")
    else:
        print(f"{nombre} no fue encontrado.")

def eliminar_superheroe():
    nombre = input("Nombre superheroe a eliminar: ").lower()
    if nombre in superheroes:
        del superheroes[nombre]
        print(f"{nombre} eliminado con éxito.")
    else:
        print(f"{nombre} no fue encontrado.")

def modificar_superheroe():
    nombre = input("Nombre superheroe: ").lower()
    if nombre in superheroes:
        fuerza = validar_positivo("Nueva fuerza: ")
        inteligencia = validar_positivo("Nueva inteligencia: ")
        superheroes[nombre] = {"fuerza": fuerza, "inteligencia": inteligencia}
        print(f"{nombre} actualizado con éxito.")
    else:
        print(f"{nombre} no fue encontrado.")

# Menú principal
menu = '''
   MENU
1. Mostrar superhéroes
2. Agregar
3. Buscar
4. Eliminar
5. Modificar
0. Salir
'''

while True:
    os.system("cls")
    opcion = input(menu)
    if opcion == "0":
        break
    elif opcion == "1":
        mostrar_superheroes()
    elif opcion == "2":
        agregar_superheroe()
    elif opcion == "3":
        buscar_superheroe()
    elif opcion == "4":
        eliminar_superheroe()
    elif opcion == "5":
        modificar_superheroe()
    else:
        print("❗ Opción incorrecta")
    input("\nPresione Enter para continuar...")

print("Gracias por utilizar el sistema de superhéroes.")
