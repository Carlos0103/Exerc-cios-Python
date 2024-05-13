import os

nome_diretorio = 'temp'
nome_arquivo = 'temp.txt'

os.makedirs(nome_diretorio, exist_ok=True)

caminho_arquivo = os.path.join(nome_diretorio, nome_arquivo)

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write("Este é o conteúdo do arquivo temp.txt\n")

print("Diretório 'temp' e arquivo 'temp.txt' foram criados com sucesso!")