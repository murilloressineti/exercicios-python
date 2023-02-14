import random

n1 = input('1º Aluno(a):')
n2 = input('2º Aluno(a):')
n3 = input('3º Aluno(a):')
n4 = input('4º Aluno(a):')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)
print(f'O aluno escolhido foi: \033[4;41m{escolhido}\033[m')
