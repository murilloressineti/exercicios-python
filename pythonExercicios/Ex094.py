pessoa = dict()
grupo = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if continua in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continua == 'N':
        break

print('-='*30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
media = soma / len(grupo)
print(f'B) A média de idade é de {media:.1f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for pessoa in grupo:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}', end=' ')
print()
print(f'D) lista das pessoas que estão acima da média: ', end='')
for pessoa in grupo:
    if pessoa['idade'] >= media:
        print('', end='')
        for keys, values in pessoa.items():
            print(f'{keys} = {values};', end=' ')
        print()
print('<<< ENCERRADO >>>>')
