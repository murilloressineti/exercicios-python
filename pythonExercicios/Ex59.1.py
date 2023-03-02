from time import sleep
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

opcao = 0
while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números  
    [ 5 ] sair do programa
    ''')
    opcao = int(input('Qual sua opção?'))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação de {n1} * {n2} é igual a {multiplicar}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        n1 = int(input('Insira o primeiro número: '))
        n2 = int(input('Insira o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Digite novamente.')
    sleep(2)
print('Fim do programa!')
