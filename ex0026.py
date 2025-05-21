frase = str(input('Digite uma frase: ')).strip()
print('A letra a apareceu em {} vezes.'.format(frase.upper().count('A')))
print('A letra a aparece pela primeira vez na {} posicao.'.format(frase.upper().find('A')+1))
print('A letra a aparece na ultima posicao em {}. '.format(frase.upper().rfind('A')+1))