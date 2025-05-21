#pessoas = {'nome': 'Karen', 'sexo': 'F', 'idade': '42'}
#print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['idade']
#pessoas['nome'] = 'João'
#pessoas['peso'] = '97.1'
#for k, v in pessoas.items():
    #print(f'{k} = {v}')
# Exercicio aula:
#Brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo','sigla': 'SP'}
#Brasil.append(estado1)
#Brasil.append(estado2)
    #print(Brasil[1]['sigla'])
estado = dict()
Brasil = list()
for c in range (0, 3):
            estado['uf'] = str(input('Unidade Federativa: '))
            estado['sigla'] = str(input('Sigla do Estado: '))
            Brasil.append(estado.copy())
#print(Brasil)
for e in Brasil:
    #for k, v in e.items():
        #print(f'O campo {k} tem valor {v}.')
     for v in e.values():
         print(v, end=' ')
     print()
