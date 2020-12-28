nome = input('qual o seu nome ')

a = nome.lower()
b = nome.upper()

c = len(nome)
c2 = nome.count(' ')
r = c - c2

d = nome.split()
d2 = len(d[0])

print('seu nome é {}, em minusculo fica {}, em maiusculo fica {}, tem {} letras ao total sendo que {} delas sao na primeira palavra'.format(nome,a,b,r,d2))

