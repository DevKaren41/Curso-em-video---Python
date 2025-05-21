from math import sqrt
a = float(input('Digite o comprimento do cateto oposto do triagulo retangulo: '))
b = float(input('Digite o comprimento do cateto adjacente do triagulo retangulo: '))
h = (a**2 + b**2)
print('O comprimento da hipotenusa è: {:.2f}cm'.format(sqrt(h)))