# Quantas aulas você tem no semestre?
# cada dia contam 3 faltas
# Aluno deve ter 75% de presença
# Aluno pode ter no máximo 25% de faltas

nome = str(input('Digite o seu nome:')).strip()
print(f'Seja bem-vindo(a) {nome}!')

aulas = int(input('Quantos dias de aula você tem no semestre?'))
aulas = aulas*3

faltas = int(input('Quantos dias você faltou?'))
faltas = faltas*3

a = 100-((faltas/aulas)*100)
print(f'Você tem {a:.0f}% de presença nas aulas.')
fr= ?
if a >= 75:
    print(f'Você ainda pode faltar {fr} dias.')
else:
    print(f'Você atingiu o limite de faltas!')

    #Preciso saber quanto representa em dias 25% das faltas.
