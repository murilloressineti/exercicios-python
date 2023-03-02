viagem = float(input('Qual a distância da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {viagem}km.')
if viagem <=200:
    print(f'O preço da sua viagem será de \033[1;32mR${(viagem*0.50):.2f}\033[m')
else:
    print(f'O preço da sua viagem será de \033[1;32mR${(viagem*0.45):.2f}\033[m')
