dist = float(input('qual a distancia da sua viajem em km '))

if dist <= 200:
    r = dist/2
    print('voce pagara {:.2f}R$ de passagem'.format(r))
else:
    r2 = dist * 0.45
    print('voce pagara {:.2f}R$ de passagem'.format(r2))
print('BOA VIAJEM CARALHO!!')

