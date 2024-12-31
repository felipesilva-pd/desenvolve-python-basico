frase = "Meu amor mora em Roma e me deu um ramo de flores"
palavra_objetivo = "amor"

# Ordenar as letras da palavra objetivo
palavra_objetivo_ordenada = sorted(palavra_objetivo)

# Separar as palavras da frase
palavras = frase.lower().split()

# Iterar sobre cada palavra da frase
for palavra in palavras:
    # Ordenar as letras da palavra atual
    palavra_ordenada = sorted(palavra)
    # Comparar as palavras ordenadas
    if palavra_ordenada == palavra_objetivo_ordenada:
        print(palavra)