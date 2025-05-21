from datetime import date
ano=int(input('Digite um ano qualquer: '))
resultado = ano%4==0 and ano%100 != 0 or ano %400 == 0
if ano == 0:
    ano=date.today().year
if resultado:
    print('O ano de {} digitado é bissexto'.format(ano))
else:
    print('O ano de {} digitado não é bissexto'.format(ano))

