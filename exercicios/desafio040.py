not1 = float(input('qual a sua nota '))
not2 = float(input('deigite outra nota '))
med = (not1 + not2)/2

if med < 5:
    print('REPROVADO')
elif med >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇAO')