veloc=float(input('Velocidade do carro?: '))
multa=(veloc-80)*7
print('A velocidade carro é: {:.0f}'.format(veloc))
if veloc>80:
    print('Sua multa sera de: {:.0f}, pois seu limite excedeu o limite permitido de 80km/h'.format(multa))
    print('Tenha um bom dia! Dirija com seguranca')
else:
    print('Nao ha multas a ser paga, voce esta dentro de limite permitido de 80 km/h')
    print('Tenha um bom dia! Dirija com seguranca')
