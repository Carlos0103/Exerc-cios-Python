arquivo_entrada = 'entradaEx7.3.txt'
arquivo_saida = 'saidaEx7.3.txt'

with open(arquivo_entrada, 'r') as arquivo_in:
    linhas_invertidas = [linha[::-1] for linha in arquivo_in]

with open(arquivo_saida, 'w') as arquivo_out:
    for linha_invertida in linhas_invertidas:
        arquivo_out.write(linha_invertida)

print("Conteúdo invertido do arquivo foi salvo em", arquivo_saida)