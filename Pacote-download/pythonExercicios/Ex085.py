num = [[], []]
valores = 0

for c in range(1, 8):
    valores = int(input(f'Digite o {c}ª valor: '))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
print('-='*20)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: \033[1;34m{num[0]}\033[m')
print(f'Os valores ímpares digitados foram: \033[1;34m{num[1]}\033[m')
