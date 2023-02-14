v1 = int(input('Primeiro valor:'))
v2 = int(input('Segundo valor:'))
v3 = int(input('Terceiro valor:'))
numeros = [v1,v2,v3]

print(f'O \033[1;4mmaior valor\033[m foi {max(numeros)}')
print(f'O \033[1;4mmenor valor\033[m foi {min(numeros)}')
