classe = input("Escolha a classe (mago, guerreiro ou arqueiro): ") # Informa a classe desejada
forca = int(input('Digite os pontos de força (de 1 a 20): ')) # Informa os pontos de força desejados
magia = int(input('Digite os pontos de magia (de 1 a 20): ')) # Informa os pontos de magia desejados

# Regras para validação dos pontos de atributos em relação a classe escolhida
mago = forca <= 10 and magia >= 15
guerreiro = forca >= 15 and magia <=10
arqueiro = ((forca > 5 and forca < 16) and (magia > 5 and magia < 16))
atributo_mago = (classe == 'mago' or classe == 'Mago') and mago
atributo_guerreiro = (classe == 'guerreiro' or classe == 'Guerreiro') and guerreiro
atributo_arqueiro = (classe == 'arqueiro' or classe == 'Arqueiro') and arqueiro

# Imprime se a classe escolhida está de acordo com os seus atributos
if classe == 'mago' or classe == 'Mago' : print("Pontos de atributo consistentes com a classe escolhida: ", atributo_mago)
elif classe == 'guerreiro' or classe == 'Guerreiro': print("Pontos de atributo consistentes com a classe escolhida: ", atributo_guerreiro)
elif classe == 'arqueiro' or classe == 'Arqueiro' : print("Pontos de atributo consistentes com a classe escolhida: ", atributo_arqueiro)

