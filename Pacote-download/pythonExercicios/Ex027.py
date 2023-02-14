nome = str(input('Digite o seu nome completo:')).strip()
print(f'Muito prazer em te conhecer \033[1;31m{nome}\033[m!')
nome = nome.split()
print(f'Seu primeiro nome é \033[1;31m{(nome[0])}\033[m.')
print(f"Seu último nome é \033[1;31m{(nome[len(nome)-1])}\033[m.")

nome2 = str(input('Digite um segundo nome completo:')).strip()
nome2 = nome2.split()

print(f'Muito prazer em te conhecer \033[1;34m{nome2[0]}\033[m!')
