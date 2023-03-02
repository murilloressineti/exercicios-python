nome = str(input('Digite o seu nome completo:')).strip()
print('Analisando o seu nome...')

print(f'Seu nome em maiúsculas é: \033[1m{nome.upper()}\033[m')
print(f'Seu nome em minúsculas é: \033[1m{nome.lower()}\033[m')
print(f"Seu nome tem ao todo \033[1m{len(nome)-nome.count(' ')} letras\033[1m")

separa = nome.split()
print(f'Seu primeiro nome tem \033[1m{len(separa[0])} letras\033[1m')
