import emoji

print('Emojis disponíveis:')
print(emoji.emojize(":red_heart:"))
print(emoji.emojize(":thumbs_up:"))
print(emoji.emojize(":thinking_face:"))
print(emoji.emojize(":partying_face:"))

frase = input('Digite uma frase e ela será emojizada:')
print(emoji.emojize(frase))