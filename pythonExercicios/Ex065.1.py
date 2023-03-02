n = 0
resposta = 'Ss'
total = 0
soma = 0
maior = menor = 0
while resposta in 'Ss':
    n = int(input('Digite um valor:'))
    soma = soma + n
    total = total + 1
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
media = soma/total
print(f'Você digitou {total} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')