soma = cont=0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num==999:
        break
    soma = soma + num
    cont+=1
print('Voce digitou {} numeros e a soma entre eles é {}!'.format(cont,soma))