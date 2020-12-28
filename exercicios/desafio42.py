import sys

a = float(input('digite um dos lados '))
b = float(input('digite outro lado '))
c = float(input('digite mais um lado '))

if (a - b) < c < (a + b) or (a - c) < b < a + c or (b - c) < a < b + c:
    print('da pra fazer um triangulo')
else:
    print('nao da pra fazer triangulo')
    sys.exit()

if a == b == c:
    print('triangulo equilatero')
    sys.exit()
if a != b != c != a:
    print('triangulo escaleno')
    sys.exit()
else:
    print('triangulo isoceles')
