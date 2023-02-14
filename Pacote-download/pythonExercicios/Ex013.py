n = input('Qual o seu nome?')
print(f'Seja bem-vindo \033[1;34m{n}\033[m!')
sa = float(input('Qual é o valor do salário atual? R$'))
pu = float(input('Qual é a porcentagem de aumento?'))
p = sa * pu / 100
t = sa + p
print(f'Com um aumento de \033[1;34m{pu}%\033[m, '
      f'o salário terá um acrescimo de \033[1;34mR${p:.2f}\033[m ficando com um total de \033[1;31mR${t:.2f}.\033[m')


