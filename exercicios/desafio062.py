a1 = int(input('dgite o primeiro termo da PA: '))
an = a1 #o a1 é uma constante entao transformei ele numa variavel igualando ele com o an
cont = 0
nval = 10 #numero de termos a ser exposto
r = int(input('digite a razao da PA: '))
while an != an + r*10:#enquanto an for diferente de a10
    an = an + r # some an com a razao
    cont += 1 # e some mais 1 na contagem de termos para ter o acompanhamento dos termos em tempo real
    print(an)
    if cont == nval: # se o numero de termos for igual ao maximo
        cont = 0 #ressetar o numero de termos pra 0
        nval = int(input('quatos termos a mais? ')) #e redefinir o maximo de termos
        if nval == 0: #se o numero de termos for redefinido para 0 o programa se encerra
            exit()
