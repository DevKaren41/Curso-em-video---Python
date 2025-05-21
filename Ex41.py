from datetime import date
atual = date.today().year
nasc = int(input('Digite sua data de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <=  9:
    print('Sua classificaçao será na categoria Mirim.')
elif idade > 9 and idade <= 14:
    print('Sua classificaçao será na categoria Infantil.')
elif idade > 14 and idade <= 19:
    print('Sua classificaçao será na categoria Junior.')
elif idade > 19 and idade <= 25:
    print('Sua classificaçao será na categoria Senior.')
else:
    print('Sua classificaçao será na categoria Master.')