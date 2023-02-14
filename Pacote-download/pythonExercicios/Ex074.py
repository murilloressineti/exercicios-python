from random import randint
random = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ',end= '')
for c in random:
    print(f'{c}',end=' ')

print(f'\nO maior valor foi {max(random)}')
print(f'O menor valor foi {min(random)}')
