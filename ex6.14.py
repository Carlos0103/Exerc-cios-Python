nomes_alunos = ['João', 'Maria', 'Pedro']
notas_alunos = [8.5, 7.2, 9.0]

lista_tuplas = [(nome, nota) for nome, nota in sorted(zip(nomes_alunos, notas_alunos), key=lambda x: x[1], reverse=True)]

print("Lista de tuplas em ordem decrescente de nota:")
for tupla in lista_tuplas:
    print(tupla)