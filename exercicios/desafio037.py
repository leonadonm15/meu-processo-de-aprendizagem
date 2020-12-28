import pyconverter

num = int(input('digite um numero '))
tipo = str(input('Voce quer o numero em decimal, hexadecimal, octal ou binario ')).lower()

bina = pyconverter.inttobin(num)
hex = pyconverter.inttohex(num)
oct = pyconverter.bintooct(bina)

if tipo == 'decimal':
    print('O numero em decimal fica {}'.format(num))
elif tipo == 'binario':
    print('O numero {} em binario fica {}'.format(num,bina))
elif tipo == 'hexadecimal':
    print('O numero {} em hexa fica {}'.format(num,hex))
elif tipo == 'octal':
    print('O numero {} em octal fica {}'.format(num,oct))
else:
    print('Voce nao colocou um tipo exitente')

print('Obrigado por vir')

