#Para 2m² de parede, é necessário 1L de tinta

a = float(input('Largura da parede?'))
l = float(input('Altura da parede?'))
print(f'Sua parede mede \033[32m{a}x{l}\033[m e sua área é de \033[31m{a*l}m²\033[m.')
print(f'Para pintar sua parede, você precisará de \033[1;31m{(a*l)/2}L\033[m de tinta.')
