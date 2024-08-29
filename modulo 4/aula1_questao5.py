n = int(input('Informe o número de participantes: ')) # Informação com o número de participantes

# Variáveis de controle
soma = 0
cont = 0

# Processamento, solicitando as idades dos participantes e atualizando as variáveis de controle
while cont < n :
    idade = int(input('Informe a idade: '))
    soma += idade
    cont += 1
print(f'A soma das idades é igual a {soma} anos.')
print(f'A média é igual a {soma/n:.0f} anos.') #Saída com a média de idade dos participantes
    