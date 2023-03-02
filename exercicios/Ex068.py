from random import randint
print(f"\033[1;33m{'-='*20}\033[m")
print('VAMOS JOGAR PAR OU ÍMPAR?')
print(f"\033[1;33m{'-='*20}\033[m")
v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    valor = ' '
    while valor not in 'PI':
        valor = str(input('Par ou Ímpar [P/I]:')).strip().upper()[0]
    print(f"\033[1;33m{'--'*20}\033[m")
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.',end= '')
    print(' \033[1mDeu PAR\033[m' if total % 2 == 0 else 'Deu \033[1mÍMPAR.\033[m')
    print(f"\033[1;33m{'--'*20}\033[m")
    if valor == 'P':
        if total % 2 == 0:
            print('\033[1;32mVOCÊ VENCEU!!!\033[m')
            v = v + 1
        else:
            print('\033[1;31mVOCÊ PERDEU!!!\033[m')
            break
    elif valor == 'I':
        if total % 2 == 1:
            print('\033[1;32mVOCÊ VENCEU!!!\033[m')
            v = v + 1
        else:
            print('\033[1;31mVOCÊ PERDEU!!!\033[m')
            break
    print(f"\033[1;32m{'-='*20}\033[m")
    print('\033[4mVamos jogar novamente...\033[m')
print(f"\033[1;35m{'-='*20}\033[m")
print(f'GAME OVER! Você conseguiu vencer \033[1m{v} vezes.\033[m')
print(f"\033[1;35m{'-='*20}\033[m")