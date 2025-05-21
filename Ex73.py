times = ('Cruzeiro', 'Bahia', 'Gremio', 'Vasco', 'Londrina', 'Sport', 'Ituano','CRB', 'Tombense',
        'Sampaio Correa','Criciúma', 'Ponte Preta', 'Novorizontino','Chapecoense','Brusque', 'CSA',
        'Operário','Guarani','Vila Nova', 'Náutico')

print (''' Opções:
[1] Os 5 primeiros times
[2] Os últimos 4 colocados
[3] Times em ordem alfabética
[4] Em que posição está o time da Chapecoense?        
''')
opcao = int(input('Qual é a opção desejada?: '))
if opcao == 1:
    print(f'Os 5 primeiros times sao: {times[0:5]}')

elif opcao == 2:
    print(f'Os ultimos 4 colocados sao: {times[16:20]}')

elif opcao == 3:
    print(f'Times em ordem alfabética: {sorted(times)}')

elif opcao == 4:
    print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
print('FIM!')




#while True:
  #  n = int(input('Digite um numero de 0 a 20: '))
    #if 0 <= time <= 20:
        #break
    #print('Tente novamente!', end='')
#print(f'O nome do time é {time[n]}.')