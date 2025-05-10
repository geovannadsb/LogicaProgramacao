#Problema 4

valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))

print("\nOperações: + - * /")
operacao = input('Qual das operações você deseja utilizar?')

if operacao == '+':
    print('O resultado é ', valor_1 + valor_2)
elif operacao == '-':
    print('O resultado é ', valor_1 - valor_2)
elif operacao == '*':
    print('O resultado é ', valor_1 * valor_2)
else:
    print('O resultado é ', valor_1 / valor_2)
