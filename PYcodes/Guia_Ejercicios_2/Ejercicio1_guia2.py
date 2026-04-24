numero = int(input("Ingresa un número: "))
multi = 1
print(f"La tabla de {numero} es:")
while multi < 11:
    prod = numero * multi
    print(f"{numero} x {multi} = {prod}")
    multi += 1