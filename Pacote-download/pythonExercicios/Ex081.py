cont = 0
n = []
while True:
    n.append(int(input('Digita um valor: ')))
    cont = cont + 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
n.sort(reverse=True)
print('-='*20)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são: {n}')
if 5 in n:
    print(f'O valor 5 faz parte da lista e foi encontrado.')
else:
    print('O valor 5 não foi encontrado na lista.')
