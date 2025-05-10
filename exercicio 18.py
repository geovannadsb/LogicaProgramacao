valor_inicial = int(input("Digite o valor final: "))
ct = 0

for number in range(valor_inicial, -1, -1):
    print(number, end=' ')
    ct += 1

print('\nQuantidade de valores gerados:', ct)