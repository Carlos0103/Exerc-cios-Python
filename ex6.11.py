numeros = [int(x) for x in input("Digite uma lista de números separados por vírgula: ").split(', ')]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", numeros_pares)