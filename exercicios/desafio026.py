frase = input('digite uma frase ')

a = len(frase)
b = frase.count('a')
c = frase.find('a')

inv = frase[::-1]
p = inv.find('a')
r = a - p



print('a letra a aparece {} vezes, aparece pela primeira vez o espaço {} e aparece pela ultima vez no espaço {}'.format(b,c,r))






