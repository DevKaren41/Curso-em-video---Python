from random import randint
from time import sleep
comp = randint(0, 5)  #faz o computador pensar
print('Vou pensar em numero entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que numero pensei? '))  #faz o jogador pensar
print('PROCESSANDO...')
sleep(4)
if jogador==comp:
    print("PARABÉNS! Voce me venceu!")
else:
    print('GANHEI! Pensei no número {} e não no {}'.format(comp,jogador))

