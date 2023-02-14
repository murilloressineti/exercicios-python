num = int(input('Insira um número de 0 a 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}...')
print(f'Unidade \033[1;31m{u}\033[m')
print(f'Dezena \033[1;31m{d}\033[m')
print(f'Centena \033[1;31m{c}\033[m')
print(f'Milhar \033[1;31m{m}\033[m')

#Esse exercício foi difícil de entender
