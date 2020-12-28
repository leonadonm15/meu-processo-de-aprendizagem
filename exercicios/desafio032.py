import sys

ano = int(input('digite o ano e vereficaremos se ele é bissexto ou nao '))

anobi = str('ano bissexto')
anono = str('ano normal')

a = ano % 400
b = ano % 100
c = ano % 4

if a == 0:
    ano = anobi
    print(anobi)
    sys.exit()

if b == 0:
    ano = anono
    print(anono)
    sys.exit()

if c == 0:
    ano = anobi
    print(anobi)
    sys.exit()
else:
    ano = anono
    print(anono)
    sys.exit()


