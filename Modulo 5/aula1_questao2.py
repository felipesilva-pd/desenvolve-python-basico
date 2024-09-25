import random
import math

n = int(input('Qual valor de n? '))

soma = 0

for i in range(n):
    numero_aleatorio = (random.randint(0, 100))
    soma += numero_aleatorio
    raiz_quadrada = math.sqrt(soma)

print(f"Quantidade de números aleatórios solicitados {n}")
print(f"Soma dos números aleatórios {soma}")
print(f"Raiz quadrada {raiz_quadrada:.2f}")