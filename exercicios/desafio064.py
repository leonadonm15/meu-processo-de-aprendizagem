val = 0
num = 0
while num != 999:
    num = int(input('digite um valor :'))
    if num != 999:
        val += num
    else:
        print('a soma dos valores foi {}'.format(val))
        exit()
