#Problema 3

valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
valor_3 = float(input("Digite o terceiro valor: "))

if valor_1>valor_2 and valor_1>valor_3:
    print('O maior valor fornecido é ', valor_1)
elif valor_2>valor_3 and valor_2>valor_1:
    print("O maior valor fornecido é ", valor_2)
else:
    print('O maior valor fornecido é ', valor_3)
