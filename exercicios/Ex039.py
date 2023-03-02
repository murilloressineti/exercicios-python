from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
diferenca = 18 - idade
diferenca2 = idade - 18

print(f'Quem nasceu em {nascimento} tem \033[4m{idade} anos\033[m em {atual}.')
if idade < 18:
    print(f'Ainda faltam \033[1;32m{diferenca} anos\033[m para o alistamento.')
    print(f'Seu alistamento será em \033[1;32m{diferenca+atual}.\033[m')
elif idade == 18:
    print('Você está na idade de se alistar.')
elif idade > 18:
    print(f'Você deveria ter se alistado há \033[1;31m{diferenca2} anos\033[m')
    print(f'Seu alistamento foi em \033[1;31m{atual-diferenca2}.\033[m')
