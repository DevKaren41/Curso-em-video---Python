nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Com notas de {} e {}, o aluno tera uma média de {}.'.format(nota1,nota2,media))
if 5.0 <= media < 6.9:
    print('Portanto o aluno esta em RECUPERAÇÃO.')
elif media < 5.0:
    print('O aluno foi REPROVADO!')
elif media >= 7.0:
    print('o aluno foi APROVADO!')