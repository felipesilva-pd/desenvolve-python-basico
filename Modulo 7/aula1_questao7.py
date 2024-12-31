import random
import string

# Lista de nomes a serem criptografados
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Gera uma chave aleatória entre 1 e 10
chave = random.randint(1, 10)

# Cria uma string com todos os caracteres visíveis
caracteres_visiveis = string.printable[:94]

# Lista para armazenar os nomes criptografados
nomes_criptografados = []

# Itera sobre cada nome
for nome in nomes:
    nome_criptografado = ""
    # Itera sobre cada letra do nome
    for letra in nome:
        # Encontra o índice da letra na string de caracteres visíveis
        indice = caracteres_visiveis.index(letra)
        # Calcula o novo índice, considerando a chave e o tamanho da string
        novo_indice = (indice + chave) % len(caracteres_visiveis)
        # Adiciona o novo caractere ao nome criptografado
        nome_criptografado += caracteres_visiveis[novo_indice]
    # Adiciona o nome criptografado à lista
    nomes_criptografados.append(nome_criptografado)

# Imprime os nomes criptografados e a chave
print(nomes_criptografados)
print("Chave:", chave)