celular = input('Digite o número: ') #Solicita ao usuario o numero de celular

# Verifica se o número possui apenas 8 digitos, adicionando o 9 no início
if len(celular) == 8:
    celular = '9' + celular
#Verifica se o primeiro digito é 9
elif len(celular) == 9:
    if celular[0] != '9':
        print('O primeiro dígito deve ser 9.')
    else:
       print(f'Número completo: {celular[:5]}-{celular[-4:]}') #Adiciona hífen entre os números do celular
