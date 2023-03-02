from datetime import date

print(f"\033[1;34m{'-='*30}\033[m")
print('\033[1;4mSEJA BEM-VINDO A CONFEDERAÇÃO BRASILEIRA DE NATAÇÃO!\033[m')
print(f"\033[1;34m{'-='*30}\033[m")

nascimento = int(input('Digite o ano de nascimento do atleta para saber sua categoria: '))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print(f'O atleta tem \033[1;4m{idade} anos\033[m e está na categoria \033[1;4;34mMIRIM.\033[m')
elif idade <= 14:
    print(f'O atleta tem \033[1;4m{idade} anos\033[m e está na categoria \033[1;4;34mINFANTIL.\033[m')
elif idade <= 19:
    print(f'O atleta tem \033[1;4m{idade} anos\033[m e está na categoria \033[1;4;34mJÚNIOR.\033[m')
elif idade <= 25:
    print(f'O atleta tem \033[1;4m{idade} anos\033[m e está na categoria \033[1;4;34mSÊNIOR.\033[m')
else:
    print(f'O atlteta tem \033[1;4m{idade} anos\033[m e está na categoria \033[1;4;34mMASTER.\033[m')
