nomes = input("Digite uma lista de nomes separados por vírgula: ").split(', ')
nomes_caixa_alta = list(map(str.upper, nomes))
print("Nomes em caixa alta:", nomes_caixa_alta)