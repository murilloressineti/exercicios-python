materiais = ('Lápis', 1.75,
             'Borracha', 2,
             'Caderno', 15.90,
             'Estojo', 25,
             'Transferidor', 4.20,
             'Compasso', 9.99,
             'Mochila', 120.32,
             'Canetas', 22.30,
             'Livro', 34.90)
print('--'*22)
print(f'\033[1;34m{"LISTAGEM DE PREÇOS":^40}\033[m')
print('--'*22)

for pos in range(0, len(materiais)):
    if pos % 2 == 0:
        print(f'{materiais[pos]:.<30}', end='')
    else:
        print(f'R${materiais[pos]:>10.2f}')
print('--'*22)
