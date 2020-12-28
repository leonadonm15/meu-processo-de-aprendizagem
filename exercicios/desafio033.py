import sys

num: float = input('digite um numero ')
num2: float = input('digite outro numero ')
num3: float = input('so mais um vai ')

'''
if num > num2 > num3:
    print('o numero {} é o maior e o menor é o numero {}'.format(num,num3))
    sys.exit()


if num3 > num2 > num:
    print('o numero {} é o maior e o menor é o numero {}'.format(num3,num))
    sys.exit()


if num2 > num3 > num:
    print('o numero {} é o maior e o menor é o numero {}'.format(num2,num))
    sys.exit()


if num3 > num > num2:
    print('o numero {} é o maior e o menor é o numero {}'.format(num3,num2))
    sys.exit()


if num2 > num > num3:
    print('o numero {} é o maior e o menor é o numero {}'.format(num2,num3))
    sys.exit()


if num > num3 >num2:
    print('o numero {} é o maior e o menor é o numero {}'.format(num,num2))
    sys.exit()
'''
maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3

menor = num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3

print('o numero {} é o maior e o menor é o numero {}'.format(maior, menor))