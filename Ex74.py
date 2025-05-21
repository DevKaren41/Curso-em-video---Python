from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
      randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end=' ')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior numero foi: {max(num)}')
print(f'O menor numero foi: {min(num)}')


