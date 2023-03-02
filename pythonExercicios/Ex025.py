#Verificar se o nome da pessoa tem 'Silva' em qualquer lugar

nome = str(input('Digite o seu nome completo:')).strip()
nome = nome.lower()
print(f"Seu nome tem Silva? \033[1;31m{('silva' in nome)}\033[m")
