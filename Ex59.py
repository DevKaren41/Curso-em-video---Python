from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Seundo valor: '))
opcao = 0
while opcao !=5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é sua opção?'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2

            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida! Tente novamente.')
    print('=-='*10)
    sleep(2)
print('Fim do programa.Volte sempre!')