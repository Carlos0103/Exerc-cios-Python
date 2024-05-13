def sugestao_roupa(clima):
   
    match clima.lower():
        case "ensolarado":
            print("Use roupas leves, boné e óculos de sol.")
        case "chuvoso":
            print("Leve um guarda-chuva e use capa de chuva.")
        case "nublado":
            print("Use uma jaqueta leve.")
        case "ventando":
            print("Proteja-se com uma blusa corta-vento.")
        case _:
            print("Use roupas confortáveis adequadas para o clima.")
            

clima = input("Digite a descrição do clima (ensolarado, chuvoso, nublado, ventando, etc.): ")

sugestao_roupa(clima)