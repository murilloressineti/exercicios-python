#Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas.
# No final do programa, mostre: a média de idade do grupo, quem é a pessoa mais velha, mais nova e o sexo
# e quantas pessoas tem menos de 18 anos.

pessoavelha = ''
pessoanova = ''
nova = 0
velha = 0
media = 0
for a in range(1, 6):
    print(f'===== {a}ª Pessoa =====')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[F/M]: ')).strip().upper()
    media = media + idade / 4
    if a == 1:
        velha = idade
        pessoavelha = nome
    if idade > velha:
        velha = idade
        pessoavelha = nome
    if a == 1:
        nova = idade
        pessoanova = nome
    if idade > nova:
        nova = idade
        pessoanova = nome
print(f'A pessoa mais velha é o(a) {pessoavelha} e tem {velha} anos.')
print(f'A pessoa mais nova é o(a) {pessoanova} e tem {nova} anos.')
print(f'A média de idade das pessoas é de {media} anos.')
