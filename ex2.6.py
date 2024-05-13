texto = input("Digite uma palavra para ser verificada se é um palíndromo: ")
if texto == texto[::-1]:
    print(f"A palavra {texto} é um palíndromo")
else:
    print(f"A palavra {texto} NÃO é um palíndromo")