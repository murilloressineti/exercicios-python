def area(l, c):
    a = l*c
    print(f'A área de um terreno é de {l}x{c} é de {a}²')

print('--'*20)
print('CONTROLE DE TERRENOS')
print('--'*20)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)
