idade_juliana = int(input("Qual sua idade, Juliana? ")) #Insere idade de Juliana
idade_cris = int(input("Qual a sua idade, Cris? ")) #Insere idade de Cris

confere_idade = idade_juliana > 17 or idade_cris > 17 #Verifica se são maiores de 18 anos

print(confere_idade) # Exibe se pelo menos uma é maior (true) ou são menores (false)