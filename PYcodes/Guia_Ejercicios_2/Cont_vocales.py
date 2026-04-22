frase = input("Ingresa una frase y veamos cuantas vocales tiene: ").strip().lower()
vocales = ["a","e","i","o","u","á","é","í","ó","ú"]
cont_vocales = 0
for letra in frase:
    if letra in vocales:
        cont_vocales += 1

print(f"la frase {frase} tiene {cont_vocales} vocales.")