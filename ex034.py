salario=float(input('Digite o salario do funconario R$: '))
if salario>1250:
    salario = (salario + (salario*0.10))
if salario<=1250:
    salario = (salario + (salario * 0.15))
print('O aumento de salario sera de R${:.2f}'.format(salario))
