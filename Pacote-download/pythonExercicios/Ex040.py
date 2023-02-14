n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1+n2)/2
if media < 5:
    print(f'\033[1;31mREPROVADO.\033[m A média do aluno foi \033[1m{media:.1f}\033[m')
elif media >= 5 and media < 7:
    print(f'\033[1;33mRECUPERAÇÃO.\033[m A média do aluno foi \033[1m{media:.1f}\033[m')
elif media >= 7:
    print(f'\033[1;32mAPROVADO.\033[m A média do aluno foi \033[1m{media:.1f}\033[m')

