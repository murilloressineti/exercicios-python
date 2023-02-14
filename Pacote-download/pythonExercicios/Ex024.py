#Verificar se o nome da cidade COMEÇA com a palavra 'Santo'

cidade = str(input('Em que cidade você nasceu?')).strip()
cidade = cidade.lower()
print(cidade[:5] == 'santo')

