from datetime import datetime

data_hora = datetime(2022, 1, 15, 12, 0)
data_formatada = data_hora.strftime("%d/%m/%Y %H:%M")
print("Data e hora:", data_formatada)