conjunto1 = {1, 2, 8, 4, 2}
conjunto2 = {4, 5, 12, 7, 10}

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
diferenca1 = conjunto1.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto1)

print("União dos conjuntos:", uniao)
print("Interseção dos conjuntos:", intersecao)
print("Diferença entre o conjunto1 e o conjunto2:", diferenca1)
print("Diferença entre o conjunto2 e o conjunto1:", diferenca2)