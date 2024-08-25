ano = int(input('Insira o ano: ')) #Solicita ao usuario que informe o ano

# Condições para saber se o número será ou não bissexto
cond1 = ano % 4 == 0
cond2 = ano % 100 != 0
cond3 = ano % 400 == 0

# Imprime o resultado de acordo com as condições estabelecidas
if ((cond1 and cond2) or cond3) :
    print('Bissexto')
else :
    print('Não Bissexto')
