valor_final = int(input("Digite o valor final: "))
ct = 0

for number in range(0, valor_final+1):
    print(number, end=' ')
    ct += 1

print('\nQuantidade de valores gerados:', ct)
