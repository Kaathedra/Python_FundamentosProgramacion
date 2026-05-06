FLETE_BASE = 5000

kilos = int(input("Ingresa los kilos de carga: "))

if kilos > 0 and kilos < 500:
    cargo_var = 100
    recargo = (kilos * cargo_var)
elif kilos >= 500 and kilos < 1000:
    cargo_var = 300
    recargo =  (kilos * cargo_var)
elif kilos > 1000:
    cargo_var = 500
    recargo = (kilos * cargo_var)
else:
    print("Error, los kilos no pueden ser negativos o cero")
print("====== DESPACHO ======")
print(f"""
    Monto fijo flete: $ {FLETE_BASE}
    Recargo Variable: $ {recargo}
    --------------------------------
    Total General:    $ {FLETE_BASE + recargo}
""")