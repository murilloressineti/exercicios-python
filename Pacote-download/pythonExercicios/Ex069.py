total = 0
homens = 0
mulheres = 0
while True:
    print('--'*20)
    print('CADASTRE UMA PESSOA')
    print('--'*20)

    idade = int(input('Idade:'))
    if idade >= 18:
        total = total + 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens = homens + 1
    elif sexo == 'F' and idade < 20:
        mulheres = mulheres + 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        print(f'Total de pessoas com mais de 18 anos: {total}')
        print(f'Ao todo temos {homens} homens cadastrados')
        print(f'E temos {mulheres} mulheres com menos de 20 anos.')
        break
print('Obrigado, volte sempre!')
