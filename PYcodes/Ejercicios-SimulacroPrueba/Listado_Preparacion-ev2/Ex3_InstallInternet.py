PLAN_DUO = 25000
INSTALACION = 15000

zona = str(input("Ingrese zona(Urbana/Rural): ".strip().lower()))

es_cliente = str(input("Es cliente nuevo? (s/n): ".strip().lower()))

estrato_client = int(input("Ingrese su estrato (1-6): ".strip().lower()))

if zona == "rural":
    if es_cliente == "s":
        PLAN_DUO = PLAN_DUO * 0.8
    else:
        PLAN_DUO = PLAN_DUO * 0.9
    if 1>=estrato_client <= 2:
        INSTALACION = INSTALACION * 0.5
    else:
        INSTALACION
elif zona == "urbana":
    if 1 >= estrato_client <= 2:
        PLAN_DUO = PLAN_DUO * 0.85
    else:
        PLAN_DUO = PLAN_DUO * 0.95
    INSTALACION = 0

print(f""" 
    -------------------------
    === Resumen de Costos ===
    Valor Plan Duo: $ {round(PLAN_DUO)}
    Costo de instalacion: $ {round(INSTALACION)}  
""")