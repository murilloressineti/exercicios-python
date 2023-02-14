# tuplas () - tuples()
# listas [] - list()
# dicionários {} - dict()

filme = {
    'título': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

print(filme['título'])

print(filme.values()) #valores (Star Wars, 1977 e George Lucas)
print(filme.keys()) #chaves (Título, ano, diretor)
print(filme.items()) #itens (todos)

for k, v in filme.items(): #k = keys and v= values ou seja: para cada chave e valor em itens, faça:
    print(f'O {k} é {v}')

pessoas = {'nome': 'Murillo', 'idade': '22', 'sexo': 'M'}
for k, v in pessoas.items():
    print(f'{k} - {v}')

#dicionários dentro de lista:

brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla'])
print(brasil[1]['sigla'])

alunos = dict()
escola = list()
for c in range(0, 2):
    alunos['nome'] = str(input('Nome do aluno: '))
    alunos['media'] = float(input('Média do aluno: '))
    escola.append(alunos.copy())
print(escola)