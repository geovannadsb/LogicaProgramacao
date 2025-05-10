print('Digite [0] para encerrar')

alunos = 0
alunos_r = 0
alunos_a = 0

while True:
    nota = float(input('Digite a nota do aluno: '))
    if nota == 0:
        break
    alunos += 1
    if nota >= 5:
        alunos_a += 1
    else:
        alunos_r += 1

print('\nQuantidade de alunos que realizaram a prova: ', alunos)
print('Quantidade de alunos reprovados: ', alunos_r)
print('Quantidade de alunos aprovados: ', alunos_a)