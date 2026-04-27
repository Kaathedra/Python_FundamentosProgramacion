cant_alumnos = int(input("Ingrese la cantidad de alumnos en el curso: "))

suma_notas = 0

aprobados = 0

reprobados = 0

for i in range(1, cant_alumnos + 1):
    nota = float(input(f"Ingrese la nota del alumno {i}: "))
    suma_notas += nota
    
    if nota >= 4.0:
        aprobados += 1
    else:
        reprobados += 1

promedio_gral = suma_notas / cant_alumnos

print("\n ==== Estadisticas del curso ====")
print(f"\nPromedio general: {round(promedio_gral, 1)}")
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos rerobados: {reprobados}")