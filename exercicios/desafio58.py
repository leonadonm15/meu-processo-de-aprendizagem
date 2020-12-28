import random
pc = random.randint(1, 10)
tent = 0
play = ''
while play != pc:
    play = int(input('Digite um numero de um a dez e vou dizer se vc acertou: '))
    tent += 1
print('acertou, eu pensei em {}, e voce conseguiu acertar em {} tentativas'.format(pc,tent))