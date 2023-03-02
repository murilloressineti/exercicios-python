#Considere US$1.00 - R$5.22
#Considere €1.00 - 5.09
#Considere £1.00 - 5.80

n = float(input('Quantos reais você tem?'))
print(f'Com R${n} você tem \033[32mUS${n/5.22:.2f}\033[m')
print(f'Com R${n} você tem \033[35m€{n/5.09:.2f}\033[m')
print(f'Com R${n} você tem \033[34m£{n/5.80:.2f}\033[m')
