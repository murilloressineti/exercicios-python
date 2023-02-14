def fatorial(n, show=False):
    """
    -> Calcula fatorial de um número
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f


fat = int(input('Digite um número para ver seu fatorial: '))
print(fatorial(fat, show=True))
