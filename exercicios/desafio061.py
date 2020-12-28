a1 = int(input('dgite o primeiro termo da PA: '))
r = int(input('digite a razao da PA: '))
an = a1
cont = 1
while an != an + r*10:
    if cont == 1:
        print(an)
    an = an + r
    cont += 1
    print(an)
    if cont == 10:
        exit()
