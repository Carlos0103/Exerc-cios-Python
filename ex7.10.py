import os
import zipfile

diretorio_textos = 'Textos'
os.makedirs(diretorio_textos, exist_ok=True)

for i in range(1, 4):
    nome_arquivo = os.path.join(diretorio_textos, f"arquivo{i}.txt")
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Python Essencial")

nome_arquivo_zip = 'textos.zip'
with zipfile.ZipFile(nome_arquivo_zip, 'w') as arquivo_zip:
    for pasta_raiz, _, arquivos in os.walk(diretorio_textos):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            arquivo_zip.write(caminho_completo, os.path.relpath(caminho_completo, diretorio_textos))

print("Arquivo compactado 'textos.zip' criado com sucesso!")