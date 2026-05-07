PLAN_DUO = 25000
INSTALACION = 15000

zona = str(input("Ingrese zona(Urbana/Rural): ".strip().lower()))

es_cliente = str(input("Es cliente nuevo? (s/n): ".strip().lower()))

estrato_client = int(input("Ingrese su estrato (1-6): ".strip().lower()))

if zona == "rural" and es_cliente == "s":
    PLAN_DUO = PLAN_DUO * 0.80
elif zona== "rural" and es_cliente == "n":
    PLAN_DUO = PLAN_DUO * 0.90
elif zona == "urbana" and estrato_client == 1 or 2:
    PLAN_DUO = PLAN_DUO * 0.85
    INSTALACION = 0
elif zona == "urbana" and estrato_client == 3 or 4 or 5 or 6:
    PLAN_DUO = PLAN_DUO * 0.95
    INSTALACION = 0
elif zona == "rural" and estrato_client == 1 or 2:
    INSTALACION = INSTALACION * 0.5


print(f""" 
    -------------------------
    === Resumen de Costos ===
    Valor Plan Duo: $ {round(PLAN_DUO)}
    Costo de instalacion: $ {round(INSTALACION)}  
""")