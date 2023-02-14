#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

media = 0
idadehomem = 0
nomehomem = ''
totmulher = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('[M/F]: ')).strip().upper()
    media = media + idade / 4
    if p == 1 and sexo == 'M':
        idadehomem = idade
        nomehomem = nome
    if sexo == 'M' and idade > idadehomem:
        idadehomem = idade
        nomehomem = nome
    if sexo == 'F' and idade <= 20:
        totmulher = totmulher + 1
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {idadehomem} anos e se chama {nomehomem}.')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos.')
