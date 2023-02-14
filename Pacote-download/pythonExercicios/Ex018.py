import math

a = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(a))
print(f'O ângulo de {a} tem o SENO de \033[1;32m{seno:.2f}\033[m')

cosseno = math.cos(math.radians(a))
print(f'O ângulo de {a} tem o COSSENO de \033[1;33m{cosseno:.2f}\033[m')

tangente = math.tan(math.radians(a))
print(f'O ângulo de {a} tem a TANGENTE de \033[1;34m{tangente:.2f}\033[m')
