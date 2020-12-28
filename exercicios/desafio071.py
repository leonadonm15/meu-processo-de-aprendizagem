def analisador(n = int(input('Digite um número: '))):
        if n >= 0:
                print('o número {} é positivo'.format(n))
        if n < 0:
                print('o número {} é negativo'.format(n))
analisador()




#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo