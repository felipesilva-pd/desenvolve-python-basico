"""Solicite uma frase do usuário e usando compreensão de listas imprima:
A lista de vogais da frase, ordenada alfabeticamente
A lista de consoantes da frase
Exemplo:
Digite uma frase: Eu gosto de programar em Python
Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']"""

frase = input("Digite uma frase para mim:") #Solicita uma frase do usuário

# Cria uma lista para armazenar as letras da frase
letras = []
for letra in frase:
    alfabeto = letra[::1] #Separa as letras da frase e adiciona a lista
    letras.append(alfabeto)

#Define as vogais e consoantes, excluindo qualquer caracter diferente, inclusive espaços
vogais = [letra for letra in letras if letra in "a,e,i,o,u,"]
consoantes = [letra for letra in letras if letra not in "a,e,i,o,u" and letra.isalpha()]

# Imprime as vogais e consoantes da frase do usuário
print(sorted(vogais))
print(consoantes)