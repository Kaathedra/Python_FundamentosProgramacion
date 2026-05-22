import math

def es_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(math.isqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

while True:
    try:
        cant_num = int(input("Ingresa la cantidad de numeros a verificar: "))
        if cant_num > 0:
            break
        else:
            print("Error: Ingresa un numero entero positivo.")
    except ValueError:
        print("Error: Ingresa solo numeros enteros.")

primo = []

no_primo = []

for i in range(cant_num):
    while True:
        try:
            numero = int(input("Ingrese el numero a verificar: "))
            if es_primo(numero):
                primo.append(numero)
            else:
                no_primo.append(numero)
            break
        except ValueError:
            print("Error: Ingresa un numero entero valido.")

print("\n--- Resultados ---")
print(f"Se ingresaron {len(primo)} numeros primos. {primo}")
print(f"Se ingresaron {len(no_primo)} numeros no primos. {no_primo}")