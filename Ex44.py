print('{:=^40}'.format(' Lojas GKA '))
preco = float(input('Digite o valor do produto:R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros
''')
opção = int(input('Qual é a opção?: '))
if opção == 1:
    total = preco - (preco * 10 / 100)
    print('O valor final de sua compra á vista no dinheiro/cheque será de: R${:.2f}.'.format(total))
elif opção == 2:
    total = preco -(preco * 5 / 100)
    print('O valor final de sua compra a vista no cartão será de: R${:.2f}.'.format(total))
elif opção == 3:
    total = preco
    parcela = total/2
    print('O valor de sua parcela sem juros dividida em 2 vezes será no valor de R${:.2f} cada uma.'.format(parcela))
elif opção == 4:
    total = preco + (preco * (20 / 100))
    totparc = int(input('Quantas parcelas?:'))
    parcela = total / totparc
    print('O valor de sua parcela com juros dividida em {:.0f} vezes e será no valor de R${:.2f} cada uma.'.format(totparc,parcela))
else:
   print('OPÇÃO INVALIDA. Tente novamente!')
