# EJERCICIO 1 para practicar Condicional if
# Solicitar el nombre y la edad de una persona
# Dependiendo de la edad se le asigna una categoria
#  [0 - 11] Infantil
#  [12 - 17] Adolescente
#  [18 - 25] Joven
#  [26 - 59] Adulto Joven
#  [60 - ...] Adulto mayor
import os
os.system("cls")

print("Bienvenido")
nombre = input("Como te llamas?: ")

while True:
    try:
        edad = int(input(f"{nombre}, por favor ingresa tu edad: "))
        if 0 <= edad < 151:
            if edad < 18:
                print(f"{nombre}, eres un infante.")
            elif edad < 26:
                print(f"{nombre}, eres un adolescente.")
            elif edad < 60:
                print(f"{nombre}, eres un adulto joven.")
            elif edad < 151:
                print(f"{nombre}, eres un adulto mayor.")
            break
        else:
            print("Error. La edad debe ser entre 0 y 150.")
    except ValueError:
        print("Error. Por favor ingresa un numero entero valido.")
        
while input("Presiona [ENTER] para finalizar el programa...") != "":
    pass