n1 = int(input('Digite um valor para n: ')) #Entrada das notas
n2 = int(input('Digite um valor para n: '))
n3 = int(input('Digite um valor para n: '))

m = (n1 + n2 + n3)/3 # Soma e cálculo da média
print(f'{m:.2f}')

# Condições para aprovação

if m >= 60 :
    print('Aprovado!')
elif m >= 40 :
    print('Recuperação')
else :
    print('Reprovado')
print('Fim')