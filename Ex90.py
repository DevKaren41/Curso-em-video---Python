# Faça um programa que leia Nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] =  str(input('Nome do(a) aluno: '))
aluno['Média'] = float(input(f'Média do(a) {aluno["Nome"]}: '))
if aluno ['Média'] >= 7:
  aluno['Situação'] = 'Aprovado'
elif 5<= aluno['Média'] < 7:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno ['Situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')




