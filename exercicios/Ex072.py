numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catoze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if n >= 0 and n <= 20:
            break
        print('Tente novamente', end=' ')
    print(f'Você digitou o número {numeros[n]}.')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        print('Fim do Programa')
        break
