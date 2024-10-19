
"""Escreva um script em Python que solicita do usuário uma quantidade indefinida de números
inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
A lista original
Os 3 primeiros elementos
Os 2 últimos elementos
A lista invertida (do fim para o começo)
Os elementos de índice par (0, 2, 4 … )
Os elementos de índice ímpar (1, 3, 5, … )"""

def obter_numeros():
  #Solicita ao usuário uma quantidade indefinida de números e os armazena em uma lista.

  numeros = []
  while True:
    try:
      numero = int(input("Digite um número (ou qualquer outro caractere para parar): "))
      numeros.append(numero)
      if len(numeros) >= 4:
        print("Você já digitou pelo menos 4 números. Deseja continuar? (s/n)")
        if input().lower() != 's':
          break
    except ValueError:
      break
  return numeros

# Obter a lista de números do usuário
lista = obter_numeros()

# Imprimir os resultados
print(f"A nossa lista é {lista}")
print(f"Os três primeiros elementos são: {lista[:3]}")
print(f"Os dois últimos elementos são: {lista[-2:]}")
print(f"A lista invertida é: {lista[::-1]}")
print(f"Os elementos de índice par são: {lista[::2]}")
print(f"Os elementos de índice impar são: {lista[1::2]}")