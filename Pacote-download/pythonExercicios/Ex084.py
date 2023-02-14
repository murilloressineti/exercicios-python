principal = list()
temporaria = list()
totpes = 0
maior = 0
menor = 0

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    totpes = totpes + 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
print('-='*40)
print(f'Ao todo você cadastrou {totpes} pessoas')
print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'{[pessoa[0]]} ', end='')
print()
print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'{[pessoa[0]]} ', end='')
print()
