genero = input('Qual seu gênero? (M ou F) ') # Solicita ao usuario que informe seu gênero
idade = int(input('Qual sua idade? ')) # Solicita ao usuário sua idade
tempo_servico = int(input('Qual seu tempo de serviço? (em anos) ')) # Solicita ao usuário seu tempo de serviço

# Verifica as condições para aposentadoria de acordo com o gênero
mulher = idade >= 60 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25)
homem = idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25)

# Imprime se pode se aposentar ou não, de acordo com condições estabelecidas
if genero == 'M' or genero == 'm' : print(homem)
elif genero == 'F' or genero == 'f' : print(mulher)