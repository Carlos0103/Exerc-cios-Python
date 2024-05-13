from datetime import datetime

instante_atual = datetime.now()
numero_semana = instante_atual.isocalendar()[1]
print(f"Instante atual: {instante_atual}")
print("Número da semana do ano:", numero_semana)