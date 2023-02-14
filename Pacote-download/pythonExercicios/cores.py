nome = str(input('Olá, insira seu nome:'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

print(f"Muito prazer {(cores['azul'])}{nome}!")
