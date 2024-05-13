def gerar_numeros_inteiros():
    numero = 1
    while True:
        yield numero
        numero += 1

gerador = gerar_numeros_inteiros()

for _ in range(10):
    print(next(gerador))