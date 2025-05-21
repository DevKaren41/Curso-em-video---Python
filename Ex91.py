from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k , v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  ==Ranking dos jogadores==')
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar:{v[0]} com {v[1]}')
    sleep(2)

## se for parte de 0, o itemgetter coloca a parte de chave, se for 1, em ordem de valor

###Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
