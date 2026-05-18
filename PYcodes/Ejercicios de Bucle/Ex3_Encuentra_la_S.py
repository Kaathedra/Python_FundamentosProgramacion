# Pide al usuario que ingrese letras una por una. Si ingresa la letra "S" (mayúscula o
# minúscula), el programa debe decir "¡Encontrada!" y usar break para dejar de pedir letras.

while True:
    letra = input("\nIngresa una letra: ").strip().lower()
    if len(letra) > 1:
        print("\nIngresa solo 1 letra")
        continue
    if letra == "s":
        print("\nEncontrada la letra 's', Adios.")
        break