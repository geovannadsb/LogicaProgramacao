soma = 0

for number in range(0,22,1):
    if number % 3 == 0:
        print(number, end=' ')
        soma = soma + number

print('\nA soma é:', soma)