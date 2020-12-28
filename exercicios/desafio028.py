import random

#escolha do computador
nu = '1 2 3 4 5'.split()
num = random.choice(nu)

#escolha de um numero randomico
lista = '1 2 3 4 5'.split()
e = random.choice(lista)


#publicaçao do resultado
print('numero que o pc escolheu: {}'.format(num))
print('numero escolhido pela inteligencia artificial: {}'.format(e))

#resultado final
if e == num:
    print('boa pc acertou!!!!!!')
else:
    print('ERROU')
print('===FIM===')



