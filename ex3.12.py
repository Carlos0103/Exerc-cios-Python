def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

soma_primos = 0

for numero in range(1, 101):
    if eh_primo(numero):
        soma_primos += numero

print(f"A soma de todos os números primos de 1 a 100 é: {soma_primos}")