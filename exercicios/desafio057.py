sexo = ''
while sexo == '':
    sexo = input('qual o seu sexo, 1- masculino, 2- feminino: ')
    if sexo == '1':
        print('sexo masculino')
        exit()
    if sexo == '2':
        print('sexo feminino')
        exit()
    else:
        sexo = ''
