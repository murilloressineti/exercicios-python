#Perguntar nome, salário, valor do imóvel e em quantos anos irá pagar
#Valor da prestação não pode exeder 30% do Salário.

print(f"\033[1;36m{'-='*30}\033[m")
print('Olá seja \033[1mBEM-VINDO(A)\033[m ao \033[4msimulador de financiamento!\033[m')
print(f"\033[1;36m{'-='*30}\033[m")

nome = str(input('Qual o seu nome?')).strip()
salario = float(input(f'{nome}, qual o seu salário?'))
imovel = float(input('Qual o valor do imóvel?'))
tempo = int(input('Em quantos anos você deseja financiar o imóvel?'))
prestacao = (imovel/(tempo*12))
print(f'O valor da sua prestação será de \033[1;33mR${prestacao:.2f}\033[m por mês.')
if prestacao > (salario*30)/100:
    print('Seu financiamento será \033[1;31mNEGADO!\033[m')
else:
    print('Seu financiamento será \033[1;34mAPROVADO!\033[m')
