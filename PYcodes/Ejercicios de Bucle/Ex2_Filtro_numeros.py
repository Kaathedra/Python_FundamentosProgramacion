# Pide al usuario 10 números. Si el número ingresado es mayor a 100, usa continue
# para ignorarlo y no sumarlo al total. Al final, muestra la suma de los números válidos.

suma = 0

for i in range (1,11):
    try:
        num = float(input(f"numero {i}: "))
        if num > 100:
            print(f"{num} ignorado para la suma")
            continue
        suma += num
    except:
        print("Excepcion")    # Podemos hacer al contador retroceder?

print(f"suma de numeros <= 100: {suma}")