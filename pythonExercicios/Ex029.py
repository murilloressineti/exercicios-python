#Velocidade permite de 80km/h
#Multa de R$7,00 para cada km/h acima do limite

velocidade = float(input('Qual a velocidade atual do seu carro?'))
if velocidade <=80:
    print('\033[1;34mVocê está dentro da velocidade permitida.\033[m')
    print('\033[1;34mTenha um bom dia! Diriga com segurança\033[m]')
else:
    print(f'\033[1;31mMULTADO! Você excedeu o limite permitido de 80km/h\033[m')
    print(f'\033[1;31mVocê deve pagar uma multa de {(velocidade-80)*7:.2f}R$!\033[m')
