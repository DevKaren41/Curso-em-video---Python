from datetime import date
atual = date.today().year
nasc = int(input('Digite sua data de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade < 18:
    saldo = 18 - idade
    print('Brevemente você irá se alistar. Ainda falta {} anos para se alistar'.format(saldo))
    ano = atual + saldo
    print('O ano de seu alistamento sera em {}'.format(ano))
elif idade == 18:
    print('Alistar-se URGENTE!')
elif idade > 18:
    saldo = idade - 18
    print('Ja passou o tempo de se alistar. Ja passaram {} anos do seu alistamento'.format(saldo))
    ano = atual - saldo
    print('O ano de seu alistamento foi em {}'.format(ano))
