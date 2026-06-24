import os

pets_presave = [
        {
            'nombre': 'lucas',
            'edad': 12,
            'peso': 5.8,
            'atencion_prioritaria': False
        },
        {
            'nombre': 'pelusa',
            'edad': 2,
            'peso': 1.5,
            'atencion_prioritaria': False
        },
        {
            'nombre': 'thor',
            'edad': 4,
            'peso': 35.0,
            'atencion_prioritaria': False
        },
        {
            'nombre': 'mimi',
            'edad': 1,
            'peso': 0.8,
            'atencion_prioritaria': False
        }
    ]


def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Menu con input
def menu():
    while True:
        clean_screen()
        print(f'''
    {'MENU PRINCIPAL':^50}
    {"="*50}
    1. Agregar mascota
    2. Buscar mascota
    3. Eliminar mascota
    4. Actualizar atencion prioritaria
    5. Mostrar mascotas
    6. Salir
            ''')
        
        try:
            opcion = int(input("\nIngrese una opcion: "))
            if opcion in [1,2,3,4,5,6]:
                return opcion
            else:
                print("\nLa opcion ingresada no existe.")
                input("\nPresione [ENTER] para continuar.")
        except ValueError:
            print("\nError: Ingrese un número entero positivo")
            input("\nPresione [ENTER] para continuar")

# Validar nombre
def validar_nombre(nombre):
    return nombre.strip() != ""

# Validar edad
def validar_edad(edad):
    return edad >= 0

#Validar peso
def validar_peso(peso):
    return peso > 0

# Agregar mascota
def agregar_mascota(mascotas_list):
    while True:
        nombre = input("\nIngrese el nombre de la mascota: ").strip().lower()
        try:
            edad = int(input("\nIngrese la edad: "))
            peso = float(input("\nIngrese su peso en Kg: "))
        except ValueError:
            print("\nError: Datos ingresados no validos.")
            return
        if validar_nombre(nombre) and validar_edad(edad) and validar_peso(peso):
            mascota = {
                'nombre':nombre,
                'edad':edad,
                'peso':peso,
                'atencion_prioritaria':False
            }
            mascotas_list.append(mascota)
            print("\nMascota registrada con exito!")
            break

# Buscar mascota
def buscar_mascota(mascotas_list, nom_mascota):
    for mascota in mascotas_list:
        if mascota['nombre'] == nom_mascota:
            print("\nMascota encontrada!")
            return mascota
    return -1

# Mostrar datos mascota
def datos_mascota(mascota):
    print(f'''
    Nombre: {mascota['nombre']}
    Edad: {mascota['edad']}
    Peso: {mascota['peso']} Kg.
    ''')
    if mascota['atencion_prioritaria']:
        print("\nAtencion: prioitaria")
    else:
        print("\nAtencion: No prioritaria")

# Ejecutar busqueda
def busqueda_mascota_exe(mascotas_list):
    nom_mascota = input("\nIngrese el nombre de la mascota: ").strip()
    mascota_encontrada = buscar_mascota(mascotas_list,nom_mascota)
    if mascota_encontrada != -1:
        datos_mascota(mascota_encontrada)
    else:
        print("\nLa mascota ingresada no se encuentra registrada.")

# Eliminar mascota
def eliminar_mascota(mascotas_list):
    nom_mascota = input("\nIngrese el nombre de la mascota a eliminar: ").strip()
    mascota_encontrada = buscar_mascota(mascotas_list,nom_mascota)
    if mascota_encontrada != -1:
        mascotas_list.remove(mascota_encontrada)
        print("\nMascota eliminada del registro con exito!")
    else:
        print("\nError: La mascota ingresada no se encuentra en el registro.")

# Actualizar atencion prioritaria
def actualizar_atencion(mascotas_list):
    for mascota in mascotas_list:
        if mascota['peso'] < 2.0 or mascota['edad'] >= 10:
            mascota['atencion_prioritaria'] = True
        else:
            mascota['atencion_prioritaria'] = False
    print("Prioridad actualizada con exito!")

# Mostrar mascotas
def mostrar_mascotas(mascotas_list):
    if len(mascotas_list) == 0:
        print("No hay mascotas registradas.")
    else:
        for i in range(len(mascotas_list)):
            print(f'''
        Nombre: {mascotas_list[i]['nombre']}
        Edad: {mascotas_list[i]['edad']}
        Peso: {mascotas_list[i]['peso']}
    ''')
            if mascotas_list[i]['atencion_prioritaria']:
                print("Nivel de atención: Prioritaria")
            else:
                print("Nivel de atención: No prioritaria")
            print("="*50)
        print("="*15,"FIN DE LA LISTA","="*15)
#=================================================#
# Orquestador del programa
def main():
    mascotas_list = []
    mascotas_list.extend(pets_presave)
    print("Lista pregenerada cargada con exito")
    input("Presiona [ENTER] para comenzar.")
    while True:
        opcion = menu()
        if opcion == 1:
            clean_screen()
            agregar_mascota(mascotas_list)
        elif opcion == 2:
            clean_screen()
            busqueda_mascota_exe(mascotas_list)
        elif opcion == 3:
            clean_screen()
            eliminar_mascota(mascotas_list)
        elif opcion == 4:
            clean_screen()
            actualizar_atencion(mascotas_list)
        elif opcion == 5:
            clean_screen()
            mostrar_mascotas(mascotas_list)
        elif opcion == 6:
            clean_screen()
            print("Saliendo del programa.")
            break
        input("\nPresiona [ENTER] para continuar")
#==================================================#
### ------> PROGRAMA PRINCIPAL <------  ###
main()