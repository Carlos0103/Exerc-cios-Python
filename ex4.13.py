frase = input("Digite uma frase: ")

palavras = frase.split()

palavras_sem_espacos = [palavra.strip() for palavra in palavras]

frase_com_espacos = ' '.join(palavras_sem_espacos)

print("Frase com espaços corrigidos:", frase_com_espacos)