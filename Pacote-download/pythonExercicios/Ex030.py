n = int(input('Me diga um número qualquer:'))
resultado = n % 2
if resultado == 0:
    print(f'O número {n} é \033[1;34mPAR!\033[m')
else:
    print(f'O número {n} é \033[1;33mIMPAR!\033[m')