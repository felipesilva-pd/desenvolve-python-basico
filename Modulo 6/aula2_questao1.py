'''1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista.
Em seguida imprima na ordem estabelecida:
A lista ordenada, sem modificar a lista original
A lista original
O índice do maior valor da lista
O índice do menor valor da lista'''

import random

# Gera 20 números aleatórios entre -100 e 100
numeros = [random.randint(-100, 100) for i in range(20)]

# Cria uma cópia ordenada da lista
lista_ordenada = sorted(numeros)
print("Lista ordenada:", lista_ordenada)

# Imprime a lista original
print("Lista original:", numeros)

# Encontra o maior e o menor valor e seus índices
maior_valor = max(numeros)
menor_valor = min(numeros)
indice_maior = numeros.index(maior_valor)
indice_menor = numeros.index(menor_valor)

# Imprime os resultados
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)