print(f"\033[1;34m{'-='*20}\033[m")
print('\033[1;4;36mCALCULE O ÍNDICE DE MASSA CORPORAL (IMC)\033[m')
print(f"\033[1;34m{'-='*20}\033[m")

peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe sua altura: '))
imc = peso/(altura**2)
print(f'O \033[1mIMC\033[m da pessoa é \033[1m{imc:.1f}\033[m')
if imc < 18.5:
    print('\033[1;34mAbaixo do peso\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[1;32mPeso ideal\033[m')
elif imc >= 25 and imc < 30:
    print('\033[1;33mSobrepeso\033[m')
elif imc >= 30 and imc < 40:
    print('\033[1;31mObesidade\033[m')
elif imc >= 40:
    print('\033[1;31mObesidade Mórbida\033[m')
