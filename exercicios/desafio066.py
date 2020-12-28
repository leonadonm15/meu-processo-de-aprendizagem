# Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input('Número 1: '))
n2 = float(input('Numero 2: '))
n3 = float(input('Numero 3: '))
menor = n1
maior = n1
if n1 == n2 == n3:                        # se os numero forem iguais, nenhum deles é maior ou menor
    print('Todos os números são iguais')
    exit()


if n2 >= maior:   # decidindo o maior numero
    maior = n2
if n3 >= maior:
    maior = n3

if n2 <= menor:  #decidindo o menor numero
    menor = n2
if n3 <= menor:
    menor = n3


print('o maior número é {} e o menor é {}'.format(maior, menor))