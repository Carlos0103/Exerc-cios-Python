class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor a ser depositado deve ser maior que zero.")
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor a ser sacado deve ser maior que zero.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para efetuar o saque.")
        self.saldo -= valor
        print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo:.2f}")

conta = ContaBancaria(100)
print("Saldo inicial:", conta.saldo)

try:
    conta.depositar(50)
    conta.sacar(30)
    conta.sacar(200) 
except ValueError as e:
    print("Erro ao operar a conta:", e)
except SaldoInsuficienteError as e:
    print("Erro ao sacar:", e)