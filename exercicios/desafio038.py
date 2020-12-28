num1 = float(input('Digite um numero '))
num2 = float(input('Digite outro numero '))
print('numero 1: {}\nnumero 2: {}'.format(num1,num2))

if num1 > num2:
    print('O numero 1 é maior ')
elif num2 > num1:
    print('O numero 2 é maior ')
else:
    print('Os números nao tem diferença ou seja sao iguais ')
