maior = 0
oper = 4
while oper == 4:
    print('='*40)
    num1 = int(input('digite um numero: '))
    num2 = int(input(('digite outro numero: ')))
    oper = input('''QUAL DAS OPERÇOES DESEJAS REALIZAR?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    --> ''')
    if oper == '1':
        print('a soma dos numeros {} e {} é {}'.format(num1,num2,num1+num2))
        oper = 4
    if oper == '2':
        print('o produto dos valores {} e {} é {}'.format(num1,num2,num1*num2))
        oper = 4
    if oper == '3':
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('o maior numero é {}'.format(maior))
        oper = 4
    if oper == '4':
        oper = 4
    if oper == '5':
        exit()
    if oper != range(1, 6):
        oper = 4



