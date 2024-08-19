# Entrada do valor inteiro referente a uma quantia em reais
valor = int(input("Digite o valor em reais: "))

# Para cada nota, calcula a quantidade de notas necessárias e o valor restante
quantidade_100 = valor // 100  # Calcula quantas notas desse valor são necessárias
valor = valor % 100        # Atualiza o valor restante

quantidade_50 = valor // 50  # Calcula quantas notas desse valor são necessárias
valor = valor % 50        # Atualiza o valor restante

quantidade_20 = valor // 20  # Calcula quantas notas desse valor são necessárias
valor = valor % 20        # Atualiza o valor restante

quantidade_10 = valor // 10  # Calcula quantas notas desse valor são necessárias
valor = valor % 10        # Atualiza o valor restante

quantidade_5 = valor // 5  # Calcula quantas notas desse valor são necessárias
valor = valor % 5        # Atualiza o valor restante

quantidade_2 = valor // 2  # Calcula quantas notas desse valor são necessárias
valor = valor % 2        # Atualiza o valor restante

quantidade_1 = valor // 1  # Calcula quantas notas desse valor são necessárias
valor = valor % 1        # Atualiza o valor restante

print(f"{quantidade_100} nota(s) de R$100,00") # Mostra a quantidade de cada nota é necessário para o valor digitado
print(f"{quantidade_50} nota(s) de R$50,00")
print(f"{quantidade_20} nota(s) de R$20,00")
print(f"{quantidade_10} nota(s) de R$10,00")
print(f"{quantidade_5} nota(s) de R$5,00")
print(f"{quantidade_2} nota(s) de R$2,00")
print(f"{quantidade_1} nota(s) de R$1,00")
