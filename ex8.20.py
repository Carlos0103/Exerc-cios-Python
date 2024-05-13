class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def mostrar_dados(self):
        print(f"{self.numerador}/{self.denominador}")

    def multiplicar(self, outra_fracao):
        novo_numerador = self.numerador * outra_fracao.numerador
        novo_denominador = self.denominador * outra_fracao.denominador
        return Fracao(novo_numerador, novo_denominador)


fracao1 = Fracao(3, 4)

print("Fração 1:")
fracao1.mostrar_dados()

fracao2 = Fracao(2, 5)

print("Fração 2:")
fracao2.mostrar_dados()

resultado_multiplicacao = fracao1.multiplicar(fracao2)
print("Resultado da multiplicação:")
resultado_multiplicacao.mostrar_dados()