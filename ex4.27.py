from datetime import datetime, timedelta

instante_especifico = datetime(2024, 5, 12, 15, 30)
instante_atualizado = instante_especifico + timedelta(days=2, hours=5)
data_formatada = instante_atualizado.strftime("%d/%m/%Y %H:%M")
print("Instante atualizado:", data_formatada)