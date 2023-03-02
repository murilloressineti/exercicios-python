def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas de alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não indicar a situação do aluno.
    :return: dicionário com informações sobre a turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'

    return r

resp = notas(5.5, 0.5, 9, 8.5, sit=True)
print(resp)
