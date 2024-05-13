import random

lista = []

for i in range(5):
    fruta = input(f"Informe o nome da fruta {i+1}: ")
    lista.append(fruta)
    
aleatoria = random.choice(lista)
print(f"Fruta aleatória: {aleatoria}")