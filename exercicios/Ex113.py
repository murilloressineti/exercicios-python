def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[1;31mErro! Por favor digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[1;31mErro! Por favor digite um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
