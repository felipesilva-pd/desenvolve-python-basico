'''2) Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada
num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a
num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:
A lista elementos
A soma dos valores da lista
A média dos valores da lista'''

import random

#Gera aleatoriamente a quantidade de elementos que nossa lista terá
num_elementos = random.randint(5, 20)
print(f"A lista terá {num_elementos} elementos.")

#Cria uma lista com números aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for i in range(num_elementos)]
# Soma e média da nossa lista
soma = sum(elementos)
media = soma / num_elementos


#Saída dos dados com as informações pedidas
print(f"Nossa lista contém os valores: {elementos}")
print(f"A soma de nossa lista é: {soma}")
print(f"A média de nossa lista é: {media:.2f}")