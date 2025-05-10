genero=input('Informe seu gênero:')
altura=float(input('Informe sua altura:'))

cm=float((62.1*altura)-44.7)
ch=float((72.7*altura)-58)

if genero=='feminino':
    print('Seu peso ideal é', cm, "kg")
elif genero=='mulher':
    print('Seu peso ideal é', cm, "kg")
else:
    print('Seu peso ideal é', ch, 'kg')