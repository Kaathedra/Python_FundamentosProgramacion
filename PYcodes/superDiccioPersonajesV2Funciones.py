# superDiccio.py
# Programa base para administrar personajes con diccionarios y funciones

import os

# Diccionario inicial con datos de personajes
personajes = {
    "goku":         {"fuerza": 16000, "inteligencia": 7000},
    "vegeta":       {"fuerza": 15500, "inteligencia": 7500},
    "naruto":       {"fuerza": 14000, "inteligencia": 7800},
    "sasuke":       {"fuerza": 13800, "inteligencia": 8200},
    "luffy":        {"fuerza": 15000, "inteligencia": 7000},
    "zoro":         {"fuerza": 14800, "inteligencia": 6900},
    "ichigo":       {"fuerza": 14500, "inteligencia": 7200},
    "tanjiro":      {"fuerza": 12500, "inteligencia": 7600},
    "eren":         {"fuerza": 13000, "inteligencia": 6800},
    "levi":         {"fuerza": 12000, "inteligencia": 8000},
    "saitama":      {"fuerza": 99999, "inteligencia": 6500},
    "gon":          {"fuerza": 11000, "inteligencia": 7000},
    "killua":       {"fuerza": 10000, "inteligencia": 8200},
    "deku":         {"fuerza": 13500, "inteligencia": 8500},
    "bakugo":       {"fuerza": 13200, "inteligencia": 8000},
    "light":        {"fuerza": 4000,  "inteligencia": 9800},
    "lelouch":      {"fuerza": 3000,  "inteligencia": 9900},
    "gintoki":      {"fuerza": 12500, "inteligencia": 7500},
    "kenshin":      {"fuerza": 12800, "inteligencia": 7700},
    "asta":         {"fuerza": 14500, "inteligencia": 7000},
}

# Menú de opciones
menu = '''
   🦸‍♂️ MENÚ personajeS
1. Mostrar personaje
2. Agregar personaje
3. Buscar personaje
4. Eliminar personaje
5. Modificar personaje
0. Salir
'''

def validar_positivo(mensaje):
    pass


def mostrar_personajes():
    pass


def agregar_personaje():
    pass


def buscar_personaje():
    pass


def eliminar_personaje():
    pass


def modificar_personaje():
    pass


# Bucle principal
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(menu)
    opcion = input("Ingrese una opción: ")

    if opcion == "0":
        print("Gracias por utilizar el superprogram. ¡Adiós!")
        break

    elif opcion == "1":
        print("\n🔍 Función para mostrar personajes aún no implementada.")
        # mostrar_personajes()

    elif opcion == "2":
        print("\n➕ Función para agregar personaje aún no implementada.")
        # agregar_personaje()

    elif opcion == "3":
        print("\n🔎 Función para buscar personaje aún no implementada.")
        # buscar_personaje()

    elif opcion == "4":
        print("\n🗑️ Función para eliminar personaje aún no implementada.")
        # eliminar_personaje()

    elif opcion == "5":
        print("\n✏️ Función para modificar personaje aún no implementada.")
        # modificar_personaje()

    else:
        print("⚠️ Opción no válida. Por favor, elija del 0 al 5.")

    input("\nPresione Enter para continuar...")

