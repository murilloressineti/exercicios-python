valor = []
pares = []
impares = []
while True:
    valor.append(int(input('Digite um valor: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
for i, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('-='*20)
print(f'A lista completa é {valor}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
