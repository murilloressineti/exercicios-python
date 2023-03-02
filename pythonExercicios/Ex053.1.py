frase = input('Digite uma frase:').strip().lower()
palavras = frase.split() #separa as palavras gerando uma lista
junto = ''.join(palavras) #junta as palavras
inverso = junto[::-1]
print(f'O inverso de {frase} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase não é um palíndromo.')