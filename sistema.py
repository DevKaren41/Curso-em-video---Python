from ex115b.lib.interface import *
from ex115b.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
   criarArq(arq)
   
while True:
    Resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if Resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif Resposta == 2:
        #Opçao de cadastrar uma nova pessoa	
        cabeçalho('Cadastrar nova pessoa')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif Resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break       
    else:
        print('\033[31mERRO!Digite uma opção válida!\033[m')
    sleep(2)
