idade_candidato = int(input('Qual a sua idade? ')) # Insere idade do candidato
quant_jogos = int(input('Quantos jogos de tabuleiro já jogou? ')) # Insere quantidade de jogos de tabuleiro do candidato
print(quant_jogos > 2) # Exibe 'True' para candidatos que jogaram mais de três jogos, e falso para menos
quant_jogos_venceu = int(input('Quantos jogos já venceu? ')) # Insere quantidade de jogos que o candidato venceu
apto = ((idade_candidato >= 16) and (idade_candidato <= 18)) and quant_jogos > 2 and quant_jogos_venceu > 0 # Verifica se o candidato está apto para realizar o ingresso no clube
print('Apto para ingressar no clube de jogos: ', apto) # Exibe se está apto (true) ou não (false)