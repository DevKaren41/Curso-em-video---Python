total = totmil= menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont+=1
    total += preco
    if preco >1000:
        totmil+=1
    if cont == 1 or preco <menor:
        menor = preco
        barato = produto
    #else:
        #if preco < menor:
         #   menor = preco
          #  barato = produto#
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM!'))
print(f'O total da compra foi de: R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o {barato} que custa R${menor}')