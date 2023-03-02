def titulo (txt):
    print('--'*20)
    print(txt)
    print('--'*20)

def area (l, c):
    l = float(input('LARGURA(m): '))
    c = float(input('COMPRIMENTO(m): '))
    resultado = l * c
    print(f'A área de um terreno de {l}x{c} é de {resultado}².')


titulo('CONTROLE DE TERRENOS')
area(0, 0)
