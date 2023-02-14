n = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
\033[1m[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL\033[m''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{n} convertido para \033[1;4mBINÁRIO\033[m é igual a \033[1;35m{bin(n)[2:]}.\033[m')
elif opcao == 2:
    print(f'{n} convertido para \033[1;4mOCTAL\033[m é igual a \033[1;35m{oct(n)[2:]}.\033[m')
elif opcao == 3:
    print(f'{n} convertido para \033[1;4mHEXADECIMAL\033[m é igual a \033[1;35m{hex(n)[2:]}.\033[m')
else:
    print('\033[1;31mOpção inválida. Tente novamente.\033[m')
