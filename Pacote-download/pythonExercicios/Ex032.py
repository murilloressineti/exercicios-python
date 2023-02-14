from datetime import date
ano = int(input('Que ano você quer analisar? Digite 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[4m{ano}\033[m \033[1;34mÉ BISSEXTO!\033[m')
else:
    print(f'O ano \033[4m{ano}\033[m \033[1;31mNÃO É BISSEXTO!\033[m')
