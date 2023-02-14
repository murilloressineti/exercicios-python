import math
v = float(input('Digite um valor:'))
print('O valor digitado foi {}, e sua porção inteira é {}'.format(v, int(v)))
print(f'O valor digitado foi \033[1;36m{v}\033[m, e sua porção inteira é \033[1;36m{int(v)}\033[m')
