lista = list()
lista.append(9)
lista.append(5)
lista.append(2)

print(lista)

#Se quiser um print melhor formato, usar enumerate:

for i, v, in enumerate(lista):
    print(f'{i}ª posição encontrei o valor {v} ')