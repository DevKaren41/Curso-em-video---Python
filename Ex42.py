print('-='*20)
print('ANALISANDOR DE TRIANGULOS')
print('-='*20)
r1 = float(input('Digite o primeiro valor da reta:'))
r2 = float(input('Digite o segundo valor da reta:'))
r3 = float(input('Digite o terceiro valor da reta:'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima PODEM FORMAR triangulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 == r2 !=r3 or r2 == r3 !=r1 or r1 == r3 != r2:
        print('Isósceles.')
    else:
        print('Escaleno.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')