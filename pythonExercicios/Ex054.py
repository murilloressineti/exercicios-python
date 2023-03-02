from datetime import date
atual = date.today().year

contmaior = 0
contmenor = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}º pessoa nasceu?'))
    idade = atual - nascimento
    if idade <= 18:
        contmenor = contmenor + 1
    else:
        contmaior = contmaior + 1
print(f'Ao todo tivemos {contmaior} pessoas maiores de idade e {contmenor} pessoas menores de idade.')
