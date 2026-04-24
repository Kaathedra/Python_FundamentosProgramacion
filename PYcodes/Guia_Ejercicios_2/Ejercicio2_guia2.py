suma = 0
while (numero := int(input("Ingresa un número: "))) >= 0:
    suma += numero
print(f"Error. No puedo sumar numeros negativos, tu resultado final es {suma}. Adiós.")