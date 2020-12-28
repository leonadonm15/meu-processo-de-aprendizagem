def progressão(linhas):
        linha = 1
        '''for linha in range(linhas):
                while True:
                        print(linha, end=" ")
                        linha += 1
                        if linha == linhas:
                                break'''

        for linha in range(linhas):
                while linha != linhas:
                        numero = range(linha)
                        print(numero)
                        linha += 1

progressão(5)

'''        for numeros in range(1,linhas):
                print(numeros, end=" ")
                numeros += 1
'''
'''
tem um contador dos valores que vao ser apresentados na sequencia, ele reflete
o numero do andar dele, logo se o contador do andar 1 for 1, o numero 1 vai ser o teto
isso vai acontecer até o numero do andar for igual ao numero de linhas escolhida pelo input

nao consegui achar a resolução do exercício, quando eu for melhor eu volto :)
'''