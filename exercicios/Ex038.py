n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
if n1 > n2:
    print(f'O \033[1;31mPRIMEIRO\033[m valor é maior.')
elif n2 > n1:
    print(f'O \033[1;31mSEGUNDO\033[m valor é maior.')
else:
    print('Não existe valor maior, os dois são \033[4miguais.\033[m')
