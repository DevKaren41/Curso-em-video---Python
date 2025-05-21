num = [2,5,9,1]
#num[2] = 3
#num.append(7)
#num.sort(reverse = True)
#num.insert(1, 3)
#if 6 in num:
 #   num.remove(6)
#else:
 #   print('Não achei o valor')
#print (num)
#print(f'Essa lista tem {len(num)} elementos.')

valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')