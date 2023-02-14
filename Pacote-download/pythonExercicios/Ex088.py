from random import randint
from time import sleep

print('-='*20)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-='*20)

lista = list()
jogos = list()

quant = int(input('Quantos jogos você quer jogar?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
print('-='*6, f' SORTEANDO {quant} JOGOS ', '-='*6)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: \033[1;34m{l}\033[m')
    sleep(1)
print('-='*6,'< BOA SORTE! > ', '-='*6)
