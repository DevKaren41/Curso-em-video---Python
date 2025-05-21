#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular#
#(largura e comprimento) e mostre a área do terreno.

def área(l, c):
    a = l * c
    print(f'A área do terreno será {a}m²')

print('Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l,c)
