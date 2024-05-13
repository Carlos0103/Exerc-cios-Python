def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if len(set(cpf)) == 1:
        return False
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito_verificador1 = 11 - (soma % 11)
    if digito_verificador1 > 9:
        digito_verificador1 = 0

    if digito_verificador1 != int(cpf[9]):
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito_verificador2 = 11 - (soma % 11)
    if digito_verificador2 > 9:
        digito_verificador2 = 0

    if digito_verificador2 != int(cpf[10]):
        return False

    return True

cpf = input("Digite o número do CPF (somente os números): ")

if validar_cpf(cpf):
    print("O CPF digitado é válido.")
else:
    print("O CPF digitado é inválido.")