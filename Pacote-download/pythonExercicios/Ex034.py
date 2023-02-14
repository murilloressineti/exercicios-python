#Para salários menores ou iguais a RS1250,00 > aumento de 15%
#Para salários maiores de > aumento de 10%

salario = float(input('Qual o salário do funcionário?'))
if salario <= 1250:
    print(f'Para quem ganhava R${salario:.2f} passará a ganhar \033[1;4mR${salario+((salario*15)/100):.2f}\033[m.')
else:
    print(f'Para quem ganhvaba R${salario:.2f} passará a ganhar \033[1;4mR${salario+((salario*10)/100):.2f}\033[m')
