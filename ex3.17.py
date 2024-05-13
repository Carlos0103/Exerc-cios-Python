numeros = []
for i in range(10):
    numero = float(input("Digite o {}º número: ".format(i + 1)))
    numeros.append(numero)

numeros_ordenados = sorted(numeros)
segundo_menor = numeros_ordenados[1]
segundo_maior = numeros_ordenados[-2]

print("O segundo menor número é:", segundo_menor)
print("O segundo maior número é:", segundo_maior)