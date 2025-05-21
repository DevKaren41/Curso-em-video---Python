print ('-='*20)
print('Cálculo IMC')
print('-='*20)
peso = float(input('Informe o peso do paciente em Kg:'))
altura = float(input('Informe a altura em metros:'))
result = peso / (altura **2)
print('O IMC dessa pessoa é {:.0f}.'.format(result))
if result <18.5:
    print('Abaixo do peso')
elif result >=18.5 and result<= 25:
   print('Peso Ideal')
elif result > 25 and result<= 30:
    print('Sobrepeso')
elif result >30 and result <= 40:
    print('Obesidade.Cuidado!')
elif result > 40:
    print('Obesidade Morbida. Precisa se cuidar com Urgência!')