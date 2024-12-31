frase = input('Digite uma frase: ')
vogais = 'aeiou'
contagem_vogais = 0

for i in frase:
    if i in vogais:
        contagem_vogais += 1

print(contagem_vogais)