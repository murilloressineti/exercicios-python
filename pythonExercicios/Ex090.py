alunos = dict()
escola = list()

for c in range(0, 1):
    alunos['nome'] = str(input('Nome: '))
    alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
    escola.append(alunos.copy())
    if alunos['média'] >= 7:
        print(f'O aluno {alunos["nome"]} foi \033[1;34mAPROVADO\033[m, pois ficou com média {alunos["média"]}')
    elif alunos['média'] >=5 and alunos['média'] <= 7:
        print(f'O aluno {alunos["nome"]} está de \033[1;33mRECUPERAÇÃO\033[m, pois ficou com méida {alunos["média"]}')
    else:
        print(f'O aluno {alunos["nome"]} foi \033[1;31mREPROVADO\033[m, pois ficou com média {alunos["média"]}')
