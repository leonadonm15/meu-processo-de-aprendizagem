f = 1
c = 0
num = int(input('Digite um numero para saber o fatorial: '))
c = num
while c > 0:
    f *= c
    c -= 1
print('o fatorial de {} é {}'.format(num, f))