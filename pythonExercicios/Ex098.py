from time import sleep

def contador(i, f, p):
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    print('--'*20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont = cont + p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont = cont - p
        print('Fim!')

#Programa principal
contador(1, 10, 1)
contador(10, 1, 1)
print('--'*20)
print('Agora é a sua vez!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
