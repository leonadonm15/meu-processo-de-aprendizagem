import cmath
a = int(input('qual o angulo'))

seno = cmath.cos(a)
coseno = cmath.sin(a)
tangente = cmath.tan(a)

print('o seno coseno e tangente de {} é {}, {}, e {}'.format(a,seno,coseno,tangente))

