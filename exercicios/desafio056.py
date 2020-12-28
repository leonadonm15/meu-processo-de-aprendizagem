mu = 0
maior = 0
soma = 0
nome_velho = ''
for i in range(0,4):
    nome = str(input('Qual o seu nome? '))
    sexo = str(input('Qual o seu sexo? '))
    id = int(input('Quantos anos voce tem? '))
    #contador de mulheres com menos de 20 anos
    if sexo == 'feminino':
        if id < 20:
            mu = mu + 1
    #homem mais velho
    if sexo == 'masculino':
        if i == 0:
            maior = id
            nome_velho = nome
        if i > 0:
            if id > maior:
                maior = id
                nome_velho = nome
    #media aritmetica das idades
    soma = soma + id
media = soma / 4

print('a media entre as idades é {:.2f}, o homem mais velho tem {} anos e se chama {} tem {} mulheres com menos de 20 anos'.format(media,maior,nome_velho,mu))
