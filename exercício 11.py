print('Para encerrar, digite [0]')

ct = 0
soma = 0
ct_2 = 0

while True:
    valor = int(input("Digite um valor real: "))
    if valor == 0:
        break
    ct += 1
    soma = soma + valor
    if valor > 20:
        ct_2 += 1

media = soma/ct
print('\nQuantidade de valores fornecidos: ',ct)
print('Soma dos valores: ', soma)
print('Média dos valores: ', media)
print('Quantidade de valores maiores que 20: ', ct_2)


