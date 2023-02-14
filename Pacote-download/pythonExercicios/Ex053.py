#Palindromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase:').strip().lower()
palavras = frase.split() #separa as palavras gerando uma lista
junto = ''.join(palavras) #junta as palavras
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print(f'O inverso de {frase} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase não é um palíndromo.')
