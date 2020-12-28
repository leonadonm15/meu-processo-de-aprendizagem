'''fat = 0
num = int(input('digite um numero: '))
for c in range(num, 1, -1):
    if c == num:
        fat = c * (c - 1)
    else:
        fat = fat * (c - 1)
print('o fatorial de {} é {}'.format(num,fat))'''#forma com for
fat = 0
const = 0
num2 = 0
num = int(input('digite um numero: '))
while num != const + 1: # o mais 1 é pra ele nao multiplicar por 0 e zerar o resultado ex: o cont ta 1 ai ele da o loop e diminui mais 1 e multiplica o resultado por 0
    if num == 1:
        print('o fatorial do numero 1 é 1')
        exit()
    if num == 0:
        fat = 1                                                                       #esse programa funciona fazendo a multiplicaçao
        print('o fatorial do num {} é {}'.format(num,fat))                            #do primeiro termo pelo segundo, depois  pegando
        exit()                                                                        #o resultado e multiplicado pelo segundo termo
    if const == 0:                                                                    #da multiplicaçao anterior menos 1, fazendo esse
        num2 = num                                                                    #processo repetidas vezes ate chegar ao resultado
        num2 -= 1
        fat = num * num2
        const += 1
    if const > 0:
        num2 -= 1
        fat = fat * num2
        const += 1
        print(const)
print('o fatorial do num {} é {}'.format(num,fat))
#ou
from math import factorial
