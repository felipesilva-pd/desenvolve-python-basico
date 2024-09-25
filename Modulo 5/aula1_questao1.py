import math

n1 = float(input('Digite o primeiro número decimal: '))
n2 = float(input('Digite o primeiro número decimal: '))

diferenca = abs(n1 - n2)
dif_arredondada = round(diferenca, 2)

print(f'A diferença absoluta entre os números {n1} e {n2} é {dif_arredondada}')