###Crie um programa que gerencie o aproveitamento de um jogador de futebol.
###O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
###de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o
###total de gols feitos durante o campeonato.
dados = dict()
partidas = list()
dados['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
dados['gols'] = partidas[:]
dados ['total'] = sum(partidas)
print('-=' * 30)
print((dados))
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {len(dados["gols"])} partidas')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i+1} fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')

