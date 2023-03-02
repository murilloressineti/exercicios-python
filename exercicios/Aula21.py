#Docstrings

def contador(i, f, p):
    """
    -> Contagem
    :param i: ínicio
    :param f: fim
    :param p: passo
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c = c + p
    print('FIM!')


contador(0, 10, 2)

help(contador)

#Argumentos Opcionais

def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}')


soma(3, 2, 5)
soma(8, 4)
soma()

#Escopo de variáveis
def teste(b):
    global a #função que faz usar a variável global
    a = 8 #Essa variável estará dentro do escopo local
    b = b + 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
#print(f'B fora vale {b}') - Dão erro por estarem fora do escopo local
#print(f'C fora vale {c}') - Dão erro por estarem fora do escopo local

#Reterno de Valores
def soma(a= 0, b= 0, c= 0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 7)
r3 = soma(8)
print(f'O resultado da soma dos valores é {r1}, {r2} e {r3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('É impar')
