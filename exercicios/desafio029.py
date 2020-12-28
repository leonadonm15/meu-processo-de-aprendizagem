v1 = int(input('Digite a velocidade do carro '))

eq = (80 - v1)*(-1)
eq2 = eq * 7


if v1 > 80:
    print('O morotorista pode correr que a 4ta serie nao tem medo de morrer')
    print('================================================================')
    print('voce ultrapassou a velocidade limite em {}KM/H pague uma multa de {}R$'.format(eq,eq2))
else:
     print('c n quer correr mais não?')
     print('pelo menos c ta dentro do limite, sem multas dessa vez')
print('BOA VIAJEM!!')
