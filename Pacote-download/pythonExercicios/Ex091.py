from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1:': randint(1, 6),
        'jogador 2:': randint(1, 6),
        'jogador 3:': randint(1, 6),
        'jogador 4:': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for keys, values in jogo.items():
    print(f'{keys} tirou {values} no dado')
    sleep(1)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for indice, valores in enumerate(ranking):
    print(f'  {indice+1}º lugar: {valores[0]} com {valores[1]} pontos')
