import random
from time import sleep
import sys
print('o jogo começa em 3 segundos')
sleep(1)
print('1')
sleep(1)
print('2')
sleep(1)
start = input(print('PC - Qual voce escolhe, pedra, papel, ou tesoura? ')).lower().strip()
pc = random.choice(['pedra','papel','tesoura'])

if start == 'pedra':
    if pc == 'tesoura':
        print('PC - Voce venceu, eu pensei em {}'.format(pc))
        sys.exit()

    if pc == 'papel':
        print('EU VENCI HAHAHAH pensei em {}'.format(pc))
        sys.exit()

    if pc == 'pedra':
        print('EMPATE')
        sys.exit()

if start == 'papel':
    if pc == 'pedra':
        print('PC - Voce venceu, eu pensei em {}').format(pc)
        sys.exit()
    if pc == 'tesoura':
        print('Perdeu misera eu pensei em {}').format(pc)
        sys.exit()
    if pc == 'papel':
        print('EMPATE')
        sys.exit()

if start == 'tesoura':
    if pc == 'papel':
        print('Voce venceu eu pensei em {}').format(pc)
        sys.exit()
    if pc == 'pedra':
        print('Perdeu mané eu pensei {} dessa vez').format(pc)
        sys.exit()
    if pc == 'tesoura':
        print('EMPATE')
        sys.exit()





