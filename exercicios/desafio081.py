#programa que tem pega nome da pessoa e idade, cadastra uma nova pessoa, ou mostra o cadastro de tod0 mundo, apenas
from time import sleep
import sistema
pergunta = 0

while pergunta != 3:
    print('=-=' * 15)
    pergunta = int(input('1 - Mostrar cadastros existentes: \n'
                         '2 - Cadastrar nova pessoa: \n'
                         '3 - Sair'
                         '                               -> '))
    print('=-=' * 15)
    sistema.novo_txt()
    if pergunta == 1:
        sistema.ler_cadastros()
    if pergunta == 2:
        sistema.novo_cadastro()

print('Saindo...')
sleep(0.5)
