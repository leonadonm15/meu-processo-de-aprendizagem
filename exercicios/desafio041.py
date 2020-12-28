import sys
id = int(input('qual a sua idade '))

if id <= 9:
    print('Voce é um nadador mirim')
    print('obrigado pela consulta')
    sys.exit()
if id <= 14:
    print('Voce é um nadador infantil')
    print('obrigado pela consulta')
    sys.exit()
if id <= 19:
    print('Voce é um ndador juvenil')
    print('obrigado pela consulta')
    sys.exit()
else:
    print('Voce é um nadador master')
print('obrigado pela consulta')
