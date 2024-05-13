def calcular_media(lista):
    try:
        if not lista:
            raise ValueError("A lista está vazia")

        numeros = []
        for elemento in lista:
            numeros.append(float(elemento))

        media = sum(numeros) / len(numeros)
        return media

    except ValueError as e:
        return str(e)
    
lista1 = [1, 2, 3, 4, 5]
print("Média da lista 1:", calcular_media(lista1))

lista2 = [10, "20", 30, "texto"]
print("Média da lista 2:", calcular_media(lista2))

lista3 = []
print("Média da lista 3:", calcular_media(lista3))