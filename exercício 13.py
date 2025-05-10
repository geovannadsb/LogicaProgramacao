print('Digite [0] para encerrar')

par = 0
soma_p = 0
impar = 0
soma_i = 0

while True:
    numero = int(input('Digite um numero: '))
    if numero == 0:
        break
    if numero %2 ==0:
        par += 1
        soma_p = soma_p + numero
    else:
        impar += 1
        soma_i = soma_i + numero

media_p = soma_p / par
media_i = soma_i / impar

print('\nA média dos números pares é: ', media_p)
print('A média dos número ímpares é: ', media_i)