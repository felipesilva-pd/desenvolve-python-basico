# Entrada do valor inteiro referente a uma quantia em reais
valor = int(input("Digite o valor em reais: "))

# Define as notas disponíveis em ordem decrescente
notas = [100, 50, 20, 10, 5, 2, 1]

# Para cada nota, calcula a quantidade de notas necessárias e o valor restante
for nota in notas:

    quantidade = valor // nota  # Calcula quantas notas desse valor são necessárias
    valor = valor % nota        # Atualiza o valor restante
    print(f"{quantidade} nota(s) de R${nota},00") # Mostra a quanditade de cada nota é necessário para o valor digitado
