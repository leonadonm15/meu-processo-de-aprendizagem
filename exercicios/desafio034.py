sal: int = input('qual o seu salario ')
x: int = 1250

if int(sal) > int(x):
    sal1 = (int(sal)/100)*10 + int(sal)
    print('como seu salario é maior que 1250$ acrescentamos 10% do valor como aumento e ficou no total de {}'.format(sal1))
else:
    sal2 = (int(sal)/100)*15 + int(sal)
    print('como seu salario é inferior a um valor estipulado, acrescentaremos 15% do mesmo a sua renda mensal, que ficara no total de {}'.format(sal2))

print('OBRIGADO PELA CONSULTA')
