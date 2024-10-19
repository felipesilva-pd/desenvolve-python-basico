'''Crie um programa em Python que receba duas listas de números do usuário,
podendo cada lista ter uma quantidade diferente de valores. Em seguida,
combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até
o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
Exemplo de interação via terminal (entradas em negrito):
Digite a quantidade de elementos da lista 1: 4
Digite os 4 elementos da lista 1:
1
2
3
4Digite a quantidade de elementos da lista 2: 6
Digite os 6 elementos da lista 2:
5
6
7
8
9
10Lista intercalada: 1 5 2 6 3 7 4 8 9 10'''


#Solicita ao usuario a quantidade de elementos da lista 1
elementos_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []

#Solicita os numeros dos elementos de acordo com a quantidade estabelecida anteriormente
for i in range(elementos_lista1):
    elemento1 = int(input(f"Digite o elemento {i+1} da lista 1: "))
    lista1.append(elemento1)

#solicita ao usuario a quantidade de elementos da lista 2
elementos_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2= []

#Solicita os numeros dos elementos de acordo com a quantidade estabelecida anteriormente
for i in range(elementos_lista2):
    elemento2 = int(input(f"Digite o elemento {i+1} da lista: "))
    lista2.append(elemento2)

#Saida com os numeros das listas
print(lista1)
print(lista2)

#Função para intercalar as duas listas retornando uma nova lista com os elementos intercalados
def intercalar_listas(lista1, lista2):
  resultado = []
  indice_lista2 = 0

  for elemento in lista1:
    resultado.append(elemento)
    if indice_lista2 < len(lista2):
      resultado.append(lista2[indice_lista2])
      indice_lista2 += 1

  # Adiciona os elementos restantes da lista2
  resultado.extend(lista2[indice_lista2:])

  return resultado

#Saída com os dados intercalados em uma nova lista
lista_intercalada = intercalar_listas(lista1, lista2)
print("Lista intercalada:", lista_intercalada)