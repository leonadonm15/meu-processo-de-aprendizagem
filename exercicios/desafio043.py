from time import sleep

print('vamos calcular seu IMC')
sleep(2)
print('BORA!!')
sleep(3)
peso = float(input('Qual seu peso? '))
altura = float(input('Qual o sua altura? '))
IMC = peso / (altura ** 2)
print('NO TRES EM')
sleep(2)
print('1')
sleep(1)
print(2)
sleep(1)
print('SEU IMC É {:.2f}'.format(IMC))

if IMC < 18.5:
    print('Voce esta abaixo do peso ideal\nENTRE 18.5 E 25')
elif IMC > 18.5 and IMC < 25:
    print('Peso ideal!!, parabens \nENTRE 18.5 E 24')
elif IMC >= 25 and IMC < 30:
    print('Sobrepeso, tem que melhorar em \nENTRE 25 E 29')
elif IMC >= 30 and IMC <= 40:
    print('OBESIDADE!!!! CUIDADO \nENTRE 30 E 40')
else:
    print('OBESIDADE MORBIDA CUIDADO SUA VIDA ESTA EM RISCO!!!\nSE CARACTERIZA PELO IMC MAIOR QUE 40')
print('obrigado pela consulta')

