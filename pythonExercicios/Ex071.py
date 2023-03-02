# considere que o caixa possui cédulas de R$100, R$50, R$20, R$10 e R$1.

print('='*30)
print(f"{'BANCO CEV':^30}")
print('='*30)
valor = int(input('Insira o valor que você quer sacar: R$'))
total = valor  #Essa variável recebe o valor que o usuário digitar
cedula = 50    #Essa variável recebe o valor da maior cédula
totcedula = 0  #Esse variável calcula quanto o programa 'banco' precisa dar para o usuário
while True:
    if total >= cedula:
        total = total - cedula
        totcedula = totcedula + 1
    else:
        if totcedula > 0: 
            print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 50: #se a cédula é maior do que o valor, o programa vai para a próxima cédula
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0 #a cada vez que muda a célula, o programa volta a 0 para contar quantas cédulas utilizou de cada
        if total == 0: #se o total chegar a 0, acabou.
            break
print('='*30)
print('Obrigado, volte sempre ao Banco CEV. Tenha um bom dia!')
