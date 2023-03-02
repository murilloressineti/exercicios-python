import random

n1 = input('1º Aluno(a):')
n2 = input('2º Aluno(a):')
n3 = input('3º Aluno(a):')
n4 = input('4º Aluno(a):')

lista = [n1, n2, n3, n4]

random.shuffle(lista)
print(f'A ordem de apresentação será:')
print(f'\033[1;31m{lista}')
