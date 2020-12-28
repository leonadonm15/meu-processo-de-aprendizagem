import datetime
soma  = 0
soma2 = 0
for c in range(0 ,7):
    ano = int(input(print('Qual seu ano de nascimento? ')))
    if 2019 - ano < 18:
        soma = soma + 1
    if 2019 - ano >= 18:
        soma2 = soma2 + 1

print('''{} pessoas abaixo de 18 anos
{} pessoas acima de 18 anos'''.format(soma,soma2))
