jogador = dict()
gols = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['jogos'] = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    gols.clear()
    for c in range(1, jogador['jogos']+1):
        gols.append(int(input(f'Quantos gols na {c}ª partida?')))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resposta == 'N':
        break

print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for dados in v.values():
        print(f'{str(dados):<15}', end='')
    print()
print('-='*30)

while True:
    busca = (int(input('Buscar dados de qual jogador? [999 para parar]'))-1)
    if busca == 998:
        break
    if busca >= (len(time)):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-='*40)
print('<<< Obrigado, volte sempre! >>>')
