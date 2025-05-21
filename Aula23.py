#print(x)
#n = int(input('Número: '))
#print(f'Você digitou o número: {n}')

#try:
 #   a = int(input('Numerador: '))
  #  b = int(input('Denominador: '))
 #   r=a/b
#except Exception as erro:
#    print(f'Erro: Não foi possível realizar a divisão! {erro.__class__}')
 #   print(f'O resultado da divisão é: {r:.1f}')
#finally:
#    print('Tente outra vez!')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r=a/b
except(ValueError, TypeError):
    print(f'Erro: Não foi possível realizar a divisão, pois o tipo de dado é inválido.')
except ZeroDivisionError:
    print(f'Erro: Não foi possível realizar a divisão por zero.')
except KeyboardInterrupt:
    print(f'Erro: O usuário não digitou os dados.')
else:
    print(f'O resultado da divisão é: {r:.1f}')
finally:
    print('Tente outra vez!')