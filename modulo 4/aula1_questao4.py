n = int(input('Informe o valor de n: ')) # Entrada da quantidade de números analisados

maior = 0 # Controle

# Processamento com a verificação da quantidade de números que serão digitados, caso n > 0
while n > 0 :
    x = int(input('Informe valor de x: '))
    if x > maior :
        maior = x

    n = n -1

print(maior) # Saída do maior numero digitado