#sistema de cadastro com arquivo gerado pelo programa
import funçoes
import time
tem_cadastro = str(input('Tem cadastro? [S/N] [R]para remoção de cadastro: ')).strip().lower()

if tem_cadastro == 's':
    funçoes.logar()
elif tem_cadastro == 'r':
    funçoes.remover_cadastro()
    funçoes.logar()
else:
    funçoes.novo_cadastro()
    print('===REDIRECIONANDO PARA LOGIN===')
    time.sleep(1)
    funçoes.logar()
