valores = tuple(int(input('Digite um número: ')) for c in range(1, 5))
print(f'Você digitou os valores {valores}')

print(f'O valor 9 apareceu {valores.count(9)} vezes')
if valores == 3:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print(f'Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=', ')
