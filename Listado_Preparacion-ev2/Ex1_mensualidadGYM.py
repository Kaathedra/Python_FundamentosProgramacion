MENSUALIDAD = 35000
EVALUACION = 20000


edad = int(input("Ingrese su edad: "))
estudiante = str(input("¿Es estudiante? (si/no): ".strip().lower()))
plan_type = str(input("Selecione el tipo de plan (anual/mensual): ".strip().lower()))

if edad < 25 and estudiante == "si":
    MENSUALIDAD = MENSUALIDAD * 0.85
elif edad < 25 and estudiante == "no":
    MENSUALIDAD = MENSUALIDAD * 0.90
elif 25 <= edad <= 59 and plan_type == "anual":
    MENSUALIDAD = MENSUALIDAD * 0.88
elif edad >= 60:
    MENSUALIDAD = MENSUALIDAD * 0.75

if plan_type == "anual" and edad < 25:
    EVALUACION = 0
elif plan_type == "anual":
    EVALUACION = EVALUACION * 0.5

print(f"""
Valor mensual: $ {round(MENSUALIDAD)}
Costo evaluacion inicial: $ {round(EVALUACION)}
""")