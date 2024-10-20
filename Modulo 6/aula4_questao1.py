"""Escreva um script python que use compreensão de listas para criar as seguintes listas:
Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
Todos os números entre 1 e 100 que sejam divisíveis por 7
Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento
(ex: ['par', 'impar',… , 'impar']) """

#Lista com os números pares de 20 até 50
lista_pares = [i for i in range(20,51,2)]
print(f"Lista dos números pares: {lista_pares}")

#Lista com os valores ao quadrado
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_quadrado = [i**2 for i in lista_original]
print(f"Lista com números ao quadrado: {lista_quadrado}")

#Lista com todos os números divisiveis por 7
lista_divisão = [i for i in range(1, 100) if i % 7 == 0]
print(f"Lista com números divisiveis por 7: {lista_divisão}")

#Lista que informa se um número é par ou impar de 0 até 30
lista_paridade = ["par" if i % 2 == 0 else "ímpar" for i in range(0, 30, 3)]
print(lista_paridade)

