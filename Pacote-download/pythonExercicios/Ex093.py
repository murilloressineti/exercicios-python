jogador = dict()
partidas = list()

jogador['jogador'] = str(input('Nome do jogador: '))
jogador['jogos'] = int(input(f'Quantas partidas {jogador["jogador"]} jogou? '))
for c in range(1, jogador['jogos']+1):
    partidas.append(int(input(f'Quantos gols na {c}ª partida? ')))
    jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)

for keys, values in jogador.items():
    print(f'O campo {keys} tem o valor: {values}')
print('-='*30)

print(f'O jogador {jogador["jogador"]} jogou {jogador["jogos"]} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'>>> Na partida {i+1}, {jogador["jogador"]} fez {v} gols')
print(f'>>> Foi um total de {jogador["total"]} gols.')
