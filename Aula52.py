num = int(input('Digite um numero: '))
tot = 0
for c in range (1,num + 1):
    if num % c ==0:
        print('\033[31m', end='')
        tot+=1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('\n\33[mO número {} foi divisível por {} vezes '.format(num,tot))
if tot == 2:
    print('É PRIMO!')
else:
    print('Não é PRIMO!')

