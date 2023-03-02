#cm = *100
#mm = *1000

medida = float(input('Insira uma distância em metros:'))
print(f'A medida em centimetros = \033[1;35m{medida*100:.0f}cm\033[m')
print(f'A medida em milimetros = \033[1;35m{medida*1000:.0f}mm\033[m')
print(f'A medida em kilmoetros= \033[1;35m{medida/1000}km\033[m')
