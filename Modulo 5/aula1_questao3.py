import random

n = random.randint(1, 10)


while True:
    palpite = int(input('Adivinhe o número entre 1 e 10:'))

    if palpite == n:
        print(f'Correto! o número é {n}')
        break
    elif palpite > n:
        print('Muito alto, tente novamente!')
    else:
        print('Muito baixo, tente novamente!')

