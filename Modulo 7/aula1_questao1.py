nome = input('Digite seu nome: ') #Solicita ao usuario que digite um nome
for i in range(len(nome)): # Imprime as letras de acordo com o número de caracteres, adicionando mais um caractere até completar o nome
    print(nome[:i+1])

