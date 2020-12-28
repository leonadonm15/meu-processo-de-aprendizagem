a1 = int(input('digite o primeiro termo da PA '))
r = int(input('digite a razao da PA '))
cont = 0
for c in range(a1,a1*r*10,r):
    cont = cont + 1
    print(c)
    if cont == 10:
        exit()
