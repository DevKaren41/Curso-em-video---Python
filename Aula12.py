nome=str(input('Qual é seu nome? '))
if nome == 'Karen':
    print('Que nome lindo!')
elif nome == "Pedro" or nome=='Joana' or nome=='Laura' :
    print('Seu nome é bem popular no Brasil!')
elif nome in "Ana Claudia Livia Paola":
    print('É um belo nome feminino!')
else:
    print('Seu nome é normal!')
print('Tenha um bom dia, {}!'.format(nome))