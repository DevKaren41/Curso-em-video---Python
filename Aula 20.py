#def mostraLinha():
    #print ('-' * 30)


#mostraLinha()
#print('Karen')
#print('Curso Python')
#print('Testes')
#mostraLinha()#


#def soma(a,b,c):
#    print(f'A= {a} e B= {b}')
 #   s= a + b + c
  #  print(f' A soma de A + B = {s}')

#soma(a=4,b=5, c=1)
#soma (5,9,5)

#def contador (* núm):
 #   tam = len(núm)
  #  print(f'Recebi os valores {núm} e são  {tam} números.')

#contador (2,1,7)
#contador (3,4)
#contador(5,8,7,12)

def dobra (lista):
    pos=0
    while pos < len(lista):
        lista[pos] *=2
        pos +=1
valores = [2, 4, 5, 7, 8]
dobra(valores)
print(valores)
