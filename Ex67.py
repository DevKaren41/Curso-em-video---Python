while True:
    n = int(input('Digite um numero para ver sua tabuada: '))
    print('-'*30)
    if n < 0:
        break
    for cont in range(1,11):
        print(f'{n} x {cont} = {n * cont}')
    print('-' * 30)
print('PROGRAMA ENCERRADO!')