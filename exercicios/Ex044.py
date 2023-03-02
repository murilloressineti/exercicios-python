#Juros no cartão com x% a cada parcela
#Opções:
#1-à vista dinheiro/cheque: 10% de desconto
#2– à vista no cartão: 5% de desconto
#3– em até 2x no cartão: preço normal
#4– 3x ou mais no cartão: 20% de juros

print(f'{"LOJAS GUANABARA":=^50}')
valor = float(input('Insira o valor TOTAL das compras: R$'))
print(f'{"FORMAS DE PAGAMENTO":=^50}')
print('''[ 1 ] à vista pix/boleto
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão com juros ''')
opcao = int(input('Selecione uma das opções acima:'))
if opcao == 1:
    print(f'Sua compra de R${valor} vai passar a custar: R${valor-(valor*10)/100:.2f}')
elif opcao == 2:
    print(f'Sua compra de R${valor} vai passar a custar: R${valor-(valor*5)/100:.2f}')
elif opcao == 3:
    print(f'Sua compra de R${valor} será parcelada em 2x de R${valor/2:.2f} SEM JUROS.')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?'))
    totparcelas = ((valor+(valor*20)/100)/parcelas)
    print(f'Sua compra de R${valor} será parcelada em {parcelas}x de R${totparcelas:.2f} COM JUROS, totalizando '
          f'R${totparcelas*parcelas:.2f}')
else:
    print('Opção inválida de pagamento.Digite Novamente.')
