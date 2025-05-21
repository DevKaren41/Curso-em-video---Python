#def somar (a,b,c=0):
   # """
    #-> Faz a som de três valores e mostra o resultado na tela.
    #:param a: o primeiro valor
    #:param b: o segundo valor
    #:param c: o terceiro valor
    #"""
    #s = a +b +c
    #print(f'A soma dos valores é: {s}')

#somar(3,4)

def fatorial (num=1):
    f = 1
    for c in range(num, 0, -1):
        f*= c
    return (f)


n =  int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')