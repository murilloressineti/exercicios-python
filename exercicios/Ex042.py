#EQUILÁTERO = TODOS OS LADOS IGUAIS
#ESCALENO = TODOS OS LADOS DIFERENTES
#ISÓSCELES = DOIS LADOS IGUAIS, UM DIFERENTE

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima \033[1;4;34mPODEM\033[m formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('\033[1;4;34mEQUILÁTERO!\033[m')
    elif l1 != l2 != l3 != l1:
        print('\033[1;4;34mESCALENO!\033[m')
    else:
        print('\033[1;4;34mISÓSCELES!\033[m')
else:
    print('Os segmento acima \033[1;4;31mNÃO PODEM\033[m formar um triângulo.')
