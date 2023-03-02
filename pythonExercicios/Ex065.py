resposta = 'S'
media = 0
soma = 0
quantidade = 0
maior = 0
menor = 0
while resposta in 'Ss':
    n = int(input('Digite um número:'))
    soma = soma + n
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma/quantidade
print(f'Você digitou {quantidade} e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
