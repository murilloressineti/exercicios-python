from random import randint
from time import sleep
computador = randint(0, 5)
print(f"\033[33m{'-='*30}\033[m")
print(f'Vou pensar em um número entre 0 e 5, tente advinhar...')
print(f"\033[33m{'-='*30}\033[m")
jogador = int(input('Em que número eu pensei?'))
print(f"\033[1;33m'PROCESSANDO...'\033[m")
sleep(2)
if jogador == computador:
    print('\033[1;32mPARABÉNS, você conseguiu me vencer!!!\033[m')
else:
    print(f'\033[1;31mGANHEI! Eu pensei no número {computador} e não no {jogador}!\033[m')
