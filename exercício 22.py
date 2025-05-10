soma = 0

print('Soma dos números inteiros que são ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos:')

for number in range(1,500+1,1):
    if number % 2 != 0 and number % 3 == 0:
        soma = soma + number
        print(soma)