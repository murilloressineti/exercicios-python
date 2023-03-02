from time import sleep
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
       [ 1 ] Somar
       [ 2 ] Multiplicar
       [ 3 ] Maior
       [ 4 ] Novos números
       [ 5 ] Sair
    ''')
    opcao = int(input('>> Escolha uma opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação entre {n1} * {n2} = {multiplicacao}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Fim do programa!')
