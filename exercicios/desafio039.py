import sys

sexo = str(input('Qual o seu sexo (feminino) ou (masculino)? ')).lower()

if sexo == 'feminino':
    print('mulheres nao tem alistamento obrigatorio')
    sys.exit()

id = int(input('Qual seu ano de nascimento? '))
ano = 2019 - id
anoda = id + 18
alist = 18 - ano

if ano == 18:
    print('O dever te chama, esta na hora de se alistar!!!')
elif ano < 18:
    print('Voce ainda nao precisa se alistar, porem faltam {} anos para tal'.format(alist))
elif ano > 18:
    print('ja passaram {} anos da sua hora de alistar, dispensado.'.format(alist * -1))



#print('voce nao precisa se alistar nas forças armadas')