n = 0
total = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    soma = soma + n
    if n != 999:
        total = total + 1
print(f'Você digitou {total} números e a soma entre eles foi {soma-999}.')
