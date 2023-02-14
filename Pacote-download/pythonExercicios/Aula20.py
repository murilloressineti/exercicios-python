#1ª FORMA:
def lin():
    print('--'*20)


lin()
print('SISTEMA DE ALUNOS')
lin()

#2ª FORMA:
def titulo(txt):
    print('--'*20)
    print(txt)
    print('--'*20)

titulo('ESCOLA CURSO EM VÍDEO')
titulo('SISTEMA DE ALUNOS')

#3ª FORMA:
def soma(a, b):
    s = a + b
    print(s)


soma(5, 5)
soma(2, 2)
soma(3, 8)
soma(a=5, b=3)
soma(b=4, a=5)

#4ª FORMA:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

soma(4, 8)
soma(a=5, b=3)

#5ª FORMA:
def contador(* num):
    print(num)


contador(1, 2, 3, 4)
contador(5, 6)
contador(7, 8, 9)

#6ª FORMA:
def contador(* num):
    for valor in num:
        print(valor)
    print('FIM!')

contador(1, 2, 3, 4)

#7ª FORMA:
def contador(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')
    print('FIM!')


contador(8, 7, 12, 70, 5)

#8ª FORMA:
def dobra (list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos = pos + 1


valores = [4, 8, 9, 0, 2]
dobra(valores)
print(valores)

#9ª FORMA:
def soma (* valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 5)
soma(5, 5, 2)
