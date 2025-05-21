#from math import factorial
#numero = int(input('Digite um numero para calcular seu fatorial: '))
#f = factorial(numero)
#print('O fatorial de {} é {}'.format(numero, f))#
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end= '')
while c>0:
    print('{}'.format(c), end = '')
    print(' x ' if c >1 else ' = ',end='' )
    f*=c
    c-=1
print('{}'.format(f))
