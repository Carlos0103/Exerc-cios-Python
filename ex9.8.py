import random
import string

def obter_palavra_secreta():
    palavras = ["python", "java", "c#", "javascript", "html", "css"]
    return random.choice(palavras)

def jogo_adivinhacao():
    palavra_secreta = obter_palavra_secreta()
    letras_adivinhadas = set()
    letras_corretas = set(palavra_secreta)
    tentativas = 5

    print("Bem-vindo ao jogo de Adivinhação de Palavras!")
    print(f"A palavra secreta tem {len(palavra_secreta)} letras.")

    while tentativas > 0:
        print("\nTentativas restantes:", tentativas)
        palavra_atual = "".join(letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta)
        print("Palavra atual:", palavra_atual)

        try:
            palpite = input("Digite uma letra: ").lower()
            if len(palpite) != 1 or palpite not in string.ascii_lowercase:
                raise ValueError("Por favor, insira uma única letra do alfabeto.")
            
            if palpite in letras_adivinhadas:
                raise ValueError("Você já tentou essa letra.")
            
            letras_adivinhadas.add(palpite)

            if palpite in letras_corretas:
                print("Letra correta!")
                if letras_corretas == letras_adivinhadas:
                    print("Parabéns! Você adivinhou a palavra secreta.")
                    return
            else:
                tentativas -= 1
                print("Letra incorreta.")
                if tentativas == 0:
                    print("Você esgotou suas tentativas. A palavra secreta era:", palavra_secreta)
                    return
        except ValueError as e:
            print("Erro:", e)

jogo_adivinhacao()