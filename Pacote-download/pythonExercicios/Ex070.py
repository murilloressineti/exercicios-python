print('--' * 20)
print('lOJA DA TECNOLOGIA')
print('--' * 20)

total = 0
mil = 0
cont = 0
menor = 0
barato = ''


while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))

    total = total + preco

    if preco > 1000:
        mil = mil + 1

    cont = cont + 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        print('---------- FIM DO PROGRAMA ----------')
        print(f'O total da compra foi de R${total:.2f}')
        print(f'Produtos custando mais de R$1000,00: {mil}')
        print(f'O Produto mais barato foi {barato} que custa R${menor:.2f}')
        break
    print('--'*20)
print(f'Obrigado, volte sempre!')