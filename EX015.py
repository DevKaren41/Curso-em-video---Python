km=float(input('Qual a quantidade de Km percorridos? '))
dias=int(input('Quantos dias foi alugado? '))
preco = (0.15*km) + (60*dias)
print('O valor total para pagamento é R${:.2f}'.format(preco))
