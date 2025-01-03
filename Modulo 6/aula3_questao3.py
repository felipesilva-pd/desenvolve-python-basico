"""Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o
intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del.
Você deve imprimir a lista antes e depois da deleção.

Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]"""

import random

#Criando uma lista aleatória
lista = [random.randint(-10, 10) for i in range(20)]

inicio_int_maior = 0
tamanho_int_maior = 0
inicio_int_atual = 0
tamanho_int_atual = 0

#Percorre nossa lista verificando a sequencia de números negativos, guardando seus respectiveis índices
for i in range(len(lista)):
    if lista[i] < 0 :
        tamanho_int_atual += 1
        if tamanho_int_atual == 1:
            inicio_int_atual = i
    else:
        if tamanho_int_atual > tamanho_int_maior:
            tamanho_int_maior = tamanho_int_atual
            inicio_int_maior = inicio_int_atual
        tamanho_int_atual = 0

#Saídas com a lista original, índices e maior sequência e nova lista após deletar maior sequência negativa
print(f"Lista original: ", lista)
print(f"O índice onde se inicia a maior sequência negativa é {inicio_int_maior}, possuindo {tamanho_int_maior} índices negativos.")
del lista[inicio_int_maior:inicio_int_maior+tamanho_int_maior]
print(lista)






