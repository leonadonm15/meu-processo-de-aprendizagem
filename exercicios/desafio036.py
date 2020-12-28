casa = float(input('Qual o preço da casa que desejas comprar? R$'))
tempo = float(input('Em quantos anos ? '))
salario = float(input('Quanto que voce ganha? R$'))
#se 30% do salario for menor sal
sal = ((salario/100)*30)
prest = casa / (tempo * 12)

if prest > sal:
    print('ERRO\nA PRESTAÇAO É MAIOR QUE 30% DO SEU SALARIO OU SEJA:\nA PRESTAÇAO {:.0f} > 30% DO SALARIO {:.0f}'.format(prest,sal))
else:
    print('APROVADO\nO PEDIODO ESTA DE ACORDO COM OS TERMOS DE 30% DO SALARIO OU SEJA:\n A PRESTAÇAO {:.0f} < 30% DO SALARIO {:.0f}'.format(prest,sal))