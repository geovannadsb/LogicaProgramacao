#Problema 5

lado_1 = float(input('Digite o primeiro lado do triângulo: '))
lado_2 = float(input('Digite o segundo lado do triângulo: '))
lado_3 = float(input('Digite o terceiro lado do triângulo: '))

if lado_1<(lado_2+lado_3) and lado_2<(lado_1+lado_3) and lado_3<(lado_1+lado_2):
    if lado_1==lado_2==lado_3:
        print('Seu triângulo é um equilátero')
    elif lado_1==lado_2 or lado_1==lado_3 or lado_2==lado_3:
        print('Seu triângulo é um isóceles')
    else:
        print('Seu triângulo é um escaleno')
else:
    print('Não há como esses lados formarem um triângulo')