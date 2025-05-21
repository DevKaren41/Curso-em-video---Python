numero = int(input('Escreva um numero inteiro qualquer: '))
print ('''Qual será a base deste número?:
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print ('{} convertido para Binário é igual a {}'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))

else:
    print('Opção Inválida. Tente novamente!')



