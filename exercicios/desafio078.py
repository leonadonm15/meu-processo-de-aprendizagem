#Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = ''.strip(), gols = 0):
    print(f'O jogador {nome} fez {gols} gols')

n = str(input('Qual o seu nome ? '))
g = str(input('Quantos gols voce fez ? '))

if g.isnumeric(): #se g for numeric, gols = g se nao, placeholder
    int(g)
elif g == '':
    g = 0
else:
    g = '</placeholder/>'

if not n.isnumeric():
    nome = n
else:
    n = '</placeholder/>'

ficha(n,g)





#|ERRO|Valor de gol nao identificado