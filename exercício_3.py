print('Informe um ponto qualquer de um plano cartesiano')
p1=float(input('x:'))
p2=float(input('y:'))

print('\nInforme outro ponto qualquer de um plano cartesiano')
q1=float(input('x:'))
q2=float(input('y:'))

distancia= ((q1-p1)**2+(q2-p2)**2)**0.5

print('A distância entre os dois pontos estabelecidos é de', distancia)