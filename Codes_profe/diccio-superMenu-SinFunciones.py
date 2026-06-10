# generar un menu para administrar los superheroes
#    MENU
# 1. Mostrar superheroes
# 2. Agregar
# 3. Buscar
# 4. Eliminar
# 5. Modificar
# 0. Salir
# obs.todos los datos quedaran guardados en minusculas
# cada vez que se realice un movimiento, se deberán mostrar 
# todos los superheroes
import os

superheroes = {
    "ironman"   : {"fuerza": 9500,  "inteligencia": 10000},
    "spiderman" : {"fuerza": 7000,  "inteligencia": 9000},
    "hulk"      : {"fuerza": 15000, "inteligencia": 4000},
}

menu = '''
   MENU
1. Mostrar superheroes
2. Agregar/Modificar
3. Buscar
4. Eliminar
5. Modificar
0. Salir
'''

while True:
    os.system("cls")
    try:
        opc = input(menu)
        if opc == "0":
            break
        elif opc == "1":
            print(f"\n{'Diccionario tabulado':^45}")
            print("-" * 45)
            print(f"{'NOMBRE':<15} {'FUERZA':^12} {'INTELIGENCIA':>12}")
            print("-" * 45)
            for clave, atributos in superheroes.items():
                print(f"{clave:<15} {atributos['fuerza']:^12} {atributos['inteligencia']:>12}")
        elif opc == "2": # agregar
            print("Agregar SuperHeroe")
            nuevo = input("Nombre superheroe: ").lower()
            if nuevo not in superheroes:
                while True: # validar fuerza
                    try:
                        fuerza = int(input("Cantidad de fuerza: "))
                        if fuerza > 0:
                            break
                    except:
                        print("⚠️ Error: no puede ser negativo")
                while True: # validar inteligencia
                    try:
                        inteligencia = int(input("Cantidad de inteligencia: "))
                        if inteligencia > 0:
                            break
                    except:
                        print("⚠️ Error: no puede ser negativo")
                superheroes[nuevo] = {"fuerza": fuerza,"inteligencia":inteligencia}
                print(f"{nuevo} agregado con exito: {superheroes[nuevo]}")   
        elif opc == "3": # buscar
            print("Buscar SuperHeroe")
            buscado = input("Nombre superheroe a buscar: ").lower()
            if buscado in superheroes:
                print(f"encontrado: {superheroes[buscado]}")
            else:
                print(f"{buscado} NO ha sido encontrado")
        elif opc == "4": # eliminar
            print("Eliminar SuperHeroe")
            elim = input("Nombre superheroe a eliminar: ").lower()
            if elim in superheroes:
                print(f"encontrado: {superheroes[elim]}")
                del superheroes[elim]
                print("eliminado con exito")
            else:
                print(f"{elim} NO ha sido encontrado")
        elif opc == "5": # modificar
            print("Actualiza datos SuperHeroe")
            buscado = input("Nombre superheroe: ").lower()
            if buscado in superheroes:
                while True: # validar fuerza
                    try:
                        fuerza = int(input("Cantidad de fuerza: "))
                        if fuerza > 0:
                            break
                    except:
                        print("⚠️ Error: no puede ser negativo")
                while True: # validar inteligencia
                    try:
                        inteligencia = int(input("Cantidad de inteligencia: "))
                        if inteligencia > 0:
                            break
                    except:
                        print("⚠️ Error: no puede ser negativo")
                superheroes[buscado] = {"fuerza": fuerza,"inteligencia":inteligencia}
                print(f"{buscado} datos actualizados: {superheroes[buscado]}")   
        else:
            print("❗ Opción incorrecta")
    except:
        print("⚠️ Error: capturado en menu")
    input("\n🧙‍♂️ Enter para continuar")
# fin menu
print("Gracias por utilizar superprogram")

