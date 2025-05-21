valorcasa = float (input('Digite o valor da casa: '))
salario = float(input('Qual é o seu salário?: '))
anos = int(input('Em quantos anos vai pagar a casa?: '))
prestação = valorcasa / (anos*12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorcasa,anos),end='')
print(' a prestação será de {:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo Concedido')
else:
    print('Empréstimo Negado')
