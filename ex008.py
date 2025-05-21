n = float(input('Digite o valor da distancia a ser lido em metros: '))
print('A medida de {} m corresponde a:'.format(n))
print('{:.6f}km'.format(n*0.0001))
print('{:.5f}hm'.format(n*0.001))
print('{:.5f}dam'.format(n*0.01))
print('{:.1f}dm'.format(n*10))
print('{:.1f}cm'.format(n*100))
print('{:.1f}mm'.format(n*1000))

