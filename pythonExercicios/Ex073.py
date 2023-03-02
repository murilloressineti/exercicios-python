times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
         'Flamengo', 'Atlético-PR', 'Atlético-MG', 'Fortaleza',
         'São Paulo', 'América-MG', 'Botafogo', 'Santos',
         'Goiás', 'Bragatino', 'Coritiba', 'Cuiabá',
         'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('-='*150)
print(f'Lista de times do Brasileirão: {times}')
print('-='*150)
print(f'Os 6 primeiros são (Libertadores): {times[0:6]}')
print('-='*150)
print(f'Os 4 últimos são (rebaixados): {times[-4:]}')
print('-='*150)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*150)
print(f'O São Paulo está na {times.index("São Paulo")+1}ª posição.')
