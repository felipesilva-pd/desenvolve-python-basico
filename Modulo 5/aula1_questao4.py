import datetime

data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime('%d/%m/%Y')
hora_formatada = data_atual.strftime('%H:%M') 

print(f'Data: {data_formatada}')
print(f'Hora: {hora_formatada}')