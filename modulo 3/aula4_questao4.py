# Solicita a entrada do peso e distancia para calculo
distancia_km = float(input('Informe a distância: '))
peso_kg = float(input('Informe o peso do pacote: '))

# Realiza o calculo do frete por Km com base na distancia
if distancia_km <= 100 :
    valor_kg = 1.00
elif distancia_km >= 101 and distancia_km <= 300 :  
    valor_kg = 1.50
else :
    valor_kg = 2.00

#Calculo do valor do frete
frete = distancia_km * valor_kg

#Taxa extra, caso o peso seja maior que 10 kg
if peso_kg > 10 :
    frete = frete + 10

#imprime resultado do frete
print(f'O frete total para o percurso é de R${frete:.2f}')



