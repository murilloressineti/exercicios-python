from random import randint
from time import sleep
import emoji
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(emoji.emojize('''Sua opções:
[ 0 ] PEDRA:mountain:
[ 1 ] PAPEL:page_with_curl:
[ 2 ] TESOURA:scissors: '''))
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(f'{"-="*15}')
print(f'O computador jogou {(itens[computador])}')
print(f'Você jogou {(itens[jogador])}')
print(f'{"-="*15}')
if computador == 0: #PEDRA
    if jogador == 0:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32mVOCÊ GANHOU!\033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR GANHOU!\033[m')
    else:
        print('Opção inválida.')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR GANHOU!\033[m')
    elif jogador == 1:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;32mVOCÊ GANHOU!\033[m')
    else:
        print('Opção inválida.')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('\033[1;32mVOCÊ GANHOU!\033[m')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR GANHOU!\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATE\033[m')
    else:
        print('Opção inválida.')
