cont = 0
soma = 0
for c in range(1,7):
    c = int(input("Digite um valor: ".format(c)))
    if c % 2 == 0:
        cont = cont + 1
        soma = soma + c
print('Voce informou {} pares e a soma deles é: {}'.format(cont, soma))
