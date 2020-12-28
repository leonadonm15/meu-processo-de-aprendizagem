import sys

preço = float(input('Qual o preço do produto? '))
tp =str(input("""1- A VISTA CHEQUE/CARTAO = 10% OFF
2- A VISTA CARTAO = 5% OFF
3- 2X NO CARTAO = PREÇO NORMAL
4- 3X OU MAIS NO CARTAO = 20% DE JUROS
RSPOSTA: """))

if tp == '1':
    print('O desconto vai ser de {}R$ ficando assim {}R$ o preço final'.format((preço/100)*10, preço - (preço/100)*10))
if tp == '2':
    print('o desconto vai ser de {}R$ ficando assim {}R$ o preço final'.format((preço/100)*5, preço - (preço/100)*5))
if tp == '3':
    print('Pagando em 2X voce nao tem desconto, a parcela fica {}R$ e o preço total a ser pago é {}'.format(preço/2, preço))
if tp == '4':
    parc = int(input('Em quantas vezes desejas parcelar? '))
    if parc < 3:
        print('ERRO')
        sys.exit()
    total = ((preço/100)*20) + preço
    print('Pagando em 3x ou mais voce tem um juros de 20%, pagando {} por parcela que no total somatizam {}'.format(total/parc,total))
print('Obrigado por comprar nas casas bahias')
