#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero_escolhido = int(input('escolha um numero entre 0 e 20 para ser escrito por extenso: '))

while numero_escolhido <= 20 and numero_escolhido >= 0:
    if numero_escolhido >= 0:
        print(extenso[numero_escolhido])
        break
    else:
        print('valor nao reconhecido')
        break
