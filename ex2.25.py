def calcular_operacao(a, b, operacao):
    match operacao:
        case '+':
            resultado = a + b
        case '-':
            resultado = a - b
        case '*':
            resultado = a * b
        case '/':
            if b != 0:
                resultado = a / b
            else:
                return "Erro: Divisão por zero!"
        case _:
            return "Erro: Operação inválida!"
    
    return resultado

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação aritmética (+, -, * ou /): ")

resultado = calcular_operacao(a, b, operacao)
print("Resultado:", resultado)