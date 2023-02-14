co = float(input('Comprimeto do cateto oposto:'))
ca = float(input('Comprimeiro do cateto adjacente:'))
print(f'A hipotenusa vai medir:\033[1;32m{((co**2 + ca**2)**(1/2)):.2f}\033[m')
