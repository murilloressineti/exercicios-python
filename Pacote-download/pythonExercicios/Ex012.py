p = float(input('Qual o preço do produto?R$'))
print(f'O produto que custava R${p}, na promoção com desconto de 5% vai custar \033[1;31mR${p-((p*5)/100)}\033[m')
