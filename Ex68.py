from random import randint
v=0
while True:
    jogador = int(input('Diga um valor: '))
    comp = randint(0,11)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {comp}, em um total de {total} jogadas.', end='')
    print('Deu PAR' if total % 2 ==0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v+=1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v+=1
        else:
            print('Você PERDEU!')
            break
        print('Vamos jogar novamente...')
    print(f'GAME OVER!Você venceu {v} vezes')
