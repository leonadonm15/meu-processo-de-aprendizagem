n = 0
t1 = 1
t2 = 0
res = 0
cont = 0

n = int(input('quantos termos da sequecia de fibonacci: '))
while n != cont:
    res = t1 + t2
    print(res)
    t1 = t2
    t2 = res
    res = 0
    cont += 1


