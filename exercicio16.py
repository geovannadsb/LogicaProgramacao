soma = 0
ct = 0

for number in range(0,11,1):
    print(number * 2, end=' ')
    ct += 1
    soma = soma + number

media = soma / ct

print('\nA soma é:', soma)
print('A média é:', media)