somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for c in range (1,5):
    print('---- {}ª pessoa -----'.format(c))
    nome = str(input('Nome:')).strip()
    sexo = str(input('Sexo[M/F]: ')).strip()
    idade = int(input('Idade: ')).strip()
    somaidade +=idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('O total de mulheres com menos de 20 anos são {}. '.format(totmulher))


