valor = int(input('Digite o valor para ser multiplicado: '))
print('Tabuada de multiplicação do número', valor, 'de um até dez:')

for number in range(1,11,1):
    multiplicacao = number*valor
    print( valor ,'x', number,' = ', multiplicacao)