num_experimentos = int(input('Informe o número total de experimentos realizados: ')) # Informa o número de experimentos que serão analisados

# Variáveis de controle
experimento = 0
soma_coelho = 0
soma_rato = 0
soma_sapo = 0

# Processamento e entrada de dados referente ao número e tipo de cobaias
while experimento < num_experimentos :
    num_cobaias = int(input('Informe o número de cobaias: '))
    tipo_cobaia = input('Informe o tipo da cobaia (S, R, C): ')
    experimento += 1
    if tipo_cobaia == 'S' or tipo_cobaia == 's' :
        soma_sapo += num_cobaias
    elif tipo_cobaia == 'R' or tipo_cobaia == 'r' :
        soma_rato += num_cobaias
    elif tipo_cobaia == 'C' or tipo_cobaia == 'c' :
        soma_coelho += num_cobaias


# Saída de dados com os totais por cobaias e seus percentuais
print('Total de Cobaias utilizadas: ', soma_coelho + soma_rato + soma_sapo)
print('Total de Coelhos: ', soma_coelho)
print('Total de Ratos: ', soma_rato)
print('Total de Sapos: ', soma_sapo)
print(f'Percentual de coelhos: {((soma_coelho/(soma_coelho + soma_rato + soma_sapo))*100):.2f}%')
print(f'Percentual de Ratos: {((soma_rato/(soma_coelho + soma_rato + soma_sapo))*100):.2f}%')
print(f'Percentual de Sapos: {((soma_sapo/(soma_coelho + soma_rato + soma_sapo))*100):.2f}%')