def decifrar_mensagem(mensagem):
    if not mensagem:
        return ""
    elif mensagem[0] == "z":
        return "a" + decifrar_mensagem(mensagem[1:])
    else:
        proxima_letra = chr(ord(mensagem[0]) + 1)
        return proxima_letra + decifrar_mensagem(mensagem[1:])

mensagem_codificada = "dzd aqzrhk"
mensagem_decodificada = decifrar_mensagem(mensagem_codificada)
print("Mensagem decodificada:", mensagem_decodificada)