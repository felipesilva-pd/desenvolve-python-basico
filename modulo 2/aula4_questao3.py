# Entrada do primeiro produto a ser comprado
produto_1 = input("Digite o nome do produto:")

# Entrada do valor unitário do primeiro produto a ser comprado
valor_unitario_1 = float(input("Digite o valor unitário do produto:"))

# Entrada da quantidade do primeiro produto a ser comprado
quantidade_1 = int(input("Digite a quantidade do produto a ser comprado:"))

# Cálculo do valor total do primeiro produto
total_1 = (quantidade_1 * valor_unitario_1)

# Entrada do segundo produto a ser comprado
produto_2 = input("Digite o nome do produto:")

# Entrada do valor unitário do segundo produto a ser comprado
valor_unitario_2 = float(input("Digite o valor unitário do produto:"))

# Entrada da quantidade do segundo produto a ser comprado
quantidade_2 = int(input("Digite a quantidade do produto a ser comprado:"))

# Cálculo do valor total do segundo produto
total_2 = (quantidade_2 * valor_unitario_2)

# Entrada do terceiro produto a ser comprado
produto_3 = input("Digite o nome do produto:")

# Entrada do valor unitário do terceiro produto a ser comprado
valor_unitario_3 = float(input("Digite o valor unitário do produto:"))

# Entrada da quantidade do terceiro produto a ser comprado
quantidade_3 = int(input("Digite a quantidade do produto a ser comprado:"))

# Cálculo do valor total do terceiro produto
total_3 = (quantidade_3 * valor_unitario_3)

# Somatório dos totais de todos os produtos
total_geral = (total_1 + total_2 + total_3)

print(f"Total: R$ {total_geral:,.2f}")