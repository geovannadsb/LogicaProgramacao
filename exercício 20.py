valor_i = int(input('Insira o valor inicial em graus Fahrenheit: '))
valor_f = int(input('Insira o valor final em graus Fahrenheit: '))

print('Fahrenheit', '|  Celsius')

for fahrenheit in range(valor_i,valor_f+1,1):
    celsius = 5/9 * (fahrenheit - 32)
    print(fahrenheit,'º       | ',f"{celsius:.3f}",'º')