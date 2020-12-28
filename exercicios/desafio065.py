menor = 0
num = 0
maior = 0
media = 0
cont = 1
resp = 'S'.upper().strip()
while resp == 'S':
    resp = str(input('Quer digitar um número? [S/N]: ').upper().strip())
    if resp == 'S':
      num = int(input('Digite um numero: '))
      if cont == 1:
          maior = num
          menor = num
      if cont > 1:
          if num <= menor:
              menor = num
          if num >= maior:
              maior = num
      media += num
      cont += 1
if cont == 0:
    exit()
if resp != 'S':
    print('A média dos numeros foi {:.2f} o maior numero foi {} e o menor foi {}'.format(media / cont, maior, menor))




