#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#Um número primo só é divisível por 1 e por ele mesmo.

numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[34m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes.')
if total == 2:
    print(f'E por isso ele é PRIMO.')
else:
    print(f'E por isso ele NÃO É PRIMO.')
