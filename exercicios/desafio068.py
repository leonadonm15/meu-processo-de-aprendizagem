def linhas(x):
        x += 1
        contador_de_linhas_v = 1
        contador_de_numeros = 1
        for contador_de_linhas_v in range(x):
                compensador = 1
                redutor = 0
                len_do_contador = len(str(contador_de_linhas_v))
                if len_do_contador == compensador:  # compensador de tamanho
                        compensador *= 10
                        redutor += 3
                if contador_de_linhas_v > 9:
                        print('{} '.format(contador_de_linhas_v) * (contador_de_linhas_v - redutor))
                else:
                        print('{} '.format(contador_de_linhas_v) * contador_de_linhas_v)
                        contador_de_linhas_v += 1
linhas(int(input('Quantidade de linhas ')))



''''
        vai receber um input que diz a quantidade de linhas
        cada linha que aumentar ganha +1 no contador e aumenta o numero monstrado
        quando igualar o contador ao x da função o bgl para

        contador de numeros horizontais
'''


#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.