while True:
    tab = int(input('Digite um número para ver sua tabuada: '))
    if tab < 0:
        break
    print('--'*10)
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab*c}')
    print('--'*10)
print('PROGRAMA ENCERRADO. Volte sempre!')
