n = input('Qual o seu nome?')
print(f'Seja bem-vindo \033[1;34m{n}\033[m!')
sa = float(input('Qual é o valor do salário atual? R$'))
pu = float(input('Qual foi a porcentagem de aumento?'))
print(f'Com um aumento de \033[1;34m{pu}%\033[m, o salário de {n} aumentou para \033[1;36m{(sa*pu/100)+sa:.2f}\033[m')
