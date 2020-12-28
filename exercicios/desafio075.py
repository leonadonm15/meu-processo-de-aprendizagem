'''
 Faça um programa de implemente um jogo de Craps.
 O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
 Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
 Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
from time import sleep
import random
contador = 0
quer_jogar = str(input('Voce quer jogar ? [S/N] ')).lower().strip()

def jogar_dado():  #função que joga o dado em si
    return random.randint(2,12)

while quer_jogar == 's':        #enquanto o jogador quiser jogar ele vai executar a função de jogar o dado, adicionar +1 ao contador de jogadas e comprar os resultados do dado com o banco de dados de numeros e seus diferentes comportamentos no jogo

    dado = jogar_dado()
    contador += 1
    vencedor_direto = [7,11]
    perdedor_direto = [2,3,12]
    pontos = [4,5,6,8,9,10]

    if contador == 1 and dado in vencedor_direto:
        print('Você é um natural, e tirou o numero {}, dentre os numeros {}, os quais garantem sua vitória na primeira rodada'.format(dado,vencedor_direto))
        exit()
    if contador == 1 and dado in perdedor_direto:
        print('Craps, você perdeu pois tirou o numero {} dentro os numeros {}, que te matam na hora :( '.format(dado,perdedor_direto))
        exit()
    if dado in pontos: #quando o dado entra no sistema de pontos a variavel dado passa o numero dela pra variavel bandeira e começa a jogar dados novamente até se encaixar em alguma das regras do jogo
        print('Você tirou o número {}'.format(dado))
        print('Você precisa tirar o numero {} denovo para vencer'.format(dado))
        bandeira = dado
        dado = 0
        while dado != bandeira:
            print('jogando mais uma vez para ver seu resultado')
            dado = jogar_dado()
            sleep(1.75)
            if dado == 7:
                print('você perdeu pois tirou sete, sad')
                exit()
            print('o valor tirado foi {}'.format(dado))
        sleep(1.75)
    print('Você venceu, pois tirou o numero {} denovo !!!'.format(bandeira))
    exit()
