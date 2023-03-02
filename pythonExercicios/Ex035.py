#Para formar um triângulo a soma dos dois triângulos precisa ser menor do que um lado.
#Se um lado do triângulo for maior do que a soma dos outros dois lados, não pode formar um triângulo.

print(f"\033[36m{'-='*20}\033[m")
print('\033[1mANALISADOR DE TRIÂNGULOS\033[m')
print(f"\033[36m{'-='*20}\033[m")

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima \033[1;4;34mPODEM\033[m formar um triângulo.')
else:
    print('Os segmento acima \033[1;4;31mNÃO PODEM\033[m formar um triângulo.')
