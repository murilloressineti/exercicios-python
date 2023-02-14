from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
    print(f'Formam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#Programa principal
maior(2, 8, 7, 4, 3)
maior(1, 9, 7, 8)
maior(4, 3, 2)
maior(8, 9)
maior(1)
maior()
