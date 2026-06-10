# vamos a definir un diccionario, por eso utilizamos { }
# cada superheroe tiene una clave única, que siempre es el primer elemento
# dentro de las {}, en este caso será el nombre que es string
# cada superheroe tendrá atributos, que corresponde a otro diccionario interno
# "fuerza" que será un entero e "inteligencia" que será entero
# para poder acceder al diccionario de algún superheroe en particular,
# necesitamos el diccionario general y la clave anotandola entre braquets []
# vamos a asignar 3 superheroes al momento de la definición
# si dejaramos el diccionario vacio la definición sería superheroes = {}

superheroes = {
    "Ironman"   : {"fuerza": 9500,  "inteligencia": 10000},
    "Spiderman" : {"fuerza": 7000,  "inteligencia": 9000},
    "Hulk"      : {"fuerza": 15000, "inteligencia": 4000},
}

# mostrar diccionario de todos los superheroes
print(f"datos de todos los superheroes:\n{superheroes}")

# mostrar diccionario de superheroe Spiderman, lo indicamos por su clave entre braquets [] 
print(f"Datos de Spiderman: {superheroes["Spiderman"]}")

# recorrer y mostrar cada item en una fila aparte
print("DICCIONARIO DE HEROES")
for nombre, atributos in superheroes.items():
    fuerza = atributos["fuerza"]
    intelig = atributos['inteligencia']
    print(f"{nombre} - Fuerza: {fuerza}, Inteligencia: {intelig}")
    
print(f"\n{'Diccionario tabulado':^45}")
print("-" * 45)
print(f"{'NOMBRE':<15} {'FUERZA':^12} {'INTELIGENCIA':>12}")
print("-" * 45)
for clave, atributos in superheroes.items():
    print(f"{clave:<15} {atributos['fuerza']:^12} {atributos['inteligencia']:>12}")

# agregando un elemento al diccionario de superheroes
# requiero ingresar la clave y luego a esa clave le asignamos el diccionario interno
# en este caso preguntamos por cuanta fuerza y por cuanta inteligencia
# lo interesante es que para agregar solo basta indicar el diccionario y la clave entre braquets
# si no existe lo agrega, si existe modifica el valor existente, sin cambiar la clave
# por lo mismo, antes de agregar debemos buscar si la clave ya ha sido ingresada
# para eso necesitamos la instruccion in
nombre = input("Super heroe a agregar: ")
if nombre not in superheroes:
    fuerza = int(input("Con cuanta fuerza: "))
    intelig = int(input("Con cuanta inteligencia: "))
    superheroes[nombre] = {"fuerza":fuerza, "inteligencia":intelig}
else:
    print(f"{nombre} ya se encuentra en la bd")
    print(f"fuerza: {superheroes[nombre]['fuerza']}")
    print(f"inteligencia: {superheroes[nombre]['inteligencia']}")

# buscar algun heroe
buscado = input("Heroe a buscar [correspondecia exacta]: ")
if buscado in superheroes:
    print("Encontrado con in")
    print(f"Su fuerza es: {superheroes[buscado]['fuerza']}")
else:
    print("NO encontrado con in")
    
# buscar item x item
encontrado = False
for clave, atributos in superheroes.items():
    # cada nombre de superheroe es la clave recuperada
    # la pasamos a minúsculas para compararla con el buscado tambien en minúsculas
    if clave.lower() == buscado.lower():
        print(f"encontrado con for: {clave} = {atributos['fuerza']}, {atributos['inteligencia']}")
        encontrado = True
        break # abandona inmediante el ciclo for despues de encontrar
    # else:
    #     print(f"NO ENCONTRADO, procesando a {clave}")
if encontrado == False:
    print(f"{buscado.lower()} No encontrado con for")
    

    