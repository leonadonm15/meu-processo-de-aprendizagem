import sys

a = float(input('digite um dos lados'))
b = float(input('digite outro lado'))
c = float(input('digite mais um lado'))

if (a - b) < c < (a + b):
    print(' da pra fazer um triangulo')
    sys.exit()
else:
    print('nao da pra fazer tringulo com os valores dados')
    sys.exit()




