"""Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50.
Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas.
Ao final imprima:
Ambas as listas
A lista intersecção ordenada
A quantidade de vezes que cada elemento aparece em cada lista
Atenção, a lista de intersecções não pode ter duplicatas. Segue um exemplo da saída esperada.
lista1 - [10, 10, 28, 10, 29, 20, 30, 10, 29, 11]
lista2 - [11, 16, 26, 44, 11, 10, 20, 29, 10, 12]
Interseccao - [10, 11, 20]
Contagem
10: (lista1=4, lista2=1)
11: (lista1=1, lista2=2)
20: (lista1=1, lista2=1)
"""

import random
from collections import Counter

#Cria nossas listas com 20 numeros aleatorios de 0 a 50
lista1 = [random.randint(0, 50) for i in range(20)]
lista2 = [random.randint(0, 50) for i in range(20)]

#Cria nossa lista de intersecao
intersecao = set(lista1).intersection(set(lista2))

#Conta a frequência que cada elemento aparece nas listas
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)


#Saida com as listas criadas
print(lista1)
print(lista2)
print(intersecao)
for elemento in intersecao:
    print(f"{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})")
