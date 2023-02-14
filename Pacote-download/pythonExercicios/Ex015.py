#Considere que o carro alugado custa R$60 por dia e R$0,15 por km rodado

d = int(input('Quantos dias o carro foi alugado?'))
km = int(input('Quantos km rodados?'))
print(f'O total a pagar é de \033[4;31mR${(60*d)+(0.15*km)}\033[m')
