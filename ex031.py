dist=float(input('Digite a distancia de sua viagem em Km: '))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O valor da passagem será no valor de: R${:.2f}'.format(preco))


