cont = 0
numero = int(input('veremos se seu numero é primo ou nao '))
for c in range(1,numero+1):
    res = numero % c
    if res == 0:
        cont = cont + 1
if cont > 2:
    print('esse numero nao é primo')
else:
    print('o numero é primo')
