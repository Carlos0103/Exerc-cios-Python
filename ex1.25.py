nome = input("Digite o nome da pessoa: ")
salario = float(input("Digite o salário da pessoa: "))
imposto = float(input("Digite o valor do imposto: "))

salario_liquido = salario - imposto
salario_formatado = "{:.2f}".format(salario_liquido)
print(f"{nome} tem um salário líquido de R$ {salario_formatado}.")