def contar_letras_a(texto):
    contador = 0
    for letra in texto:
        if letra.lower() == 'a':
            contador += 1
    if contador > 0:
        return f"A letra 'a' aparece {contador} vezes."
    else:
        return "A letra 'a' não aparece na string."

texto = input("Digite uma string: ")
print(contar_letras_a(texto))
