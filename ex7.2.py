nome_arquivo = arquivo_saida = 'arquivoEx7.2.txt'

contador_linhas = 0

with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        contador_linhas += 1

print(f"O arquivo '{nome_arquivo}' possui {contador_linhas} linhas.")