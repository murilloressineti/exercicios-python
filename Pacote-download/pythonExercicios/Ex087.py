matriz = [[], [], []]
somap = somatc = maiorsl = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]:')))
print('-='*20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somap = somap + matriz[linha][coluna]
    print()
print('-='*20)
print(f'A soma dos valores pares é {somap}') #Soma dos valores pares digitados

for linha in range(0, 3):
    somatc = somatc + matriz[linha][2]
print(f'A soma dos valores da terceira coluna {somatc}') #Soma dos valores da terceira coluna

for coluna in range(0, 3): #Maior valor apenas da segunda linha
    if coluna == 0:
        maiorsl = matriz[1][coluna]
    elif matriz[1][coluna] > maiorsl:
        maiorsl = matriz[1][coluna]
print(f'O maior valor da segunda linha {maiorsl}')
