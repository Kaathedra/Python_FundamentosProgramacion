print("Veamos como te fue en tu examen")
while True:
    try:
        nota_final = float(input("Ingresa tu nota final: "))
        if nota_final > 0 and nota_final < 4:
            print("Reprobado.")
        elif nota_final > 4 and nota_final <=5.9:
            print("Aprobado.")
        elif nota_final >= 6 and nota_final < 7:
            print("Aprobado con distincion.")
        break
    except ValueError():
        print("Error. Ingresa una nota valida.")