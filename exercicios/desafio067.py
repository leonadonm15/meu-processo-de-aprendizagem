digitar_numero = str(input('voce quer digitar um numero? [S/N] ')).strip().lower()
lista = []
maior = 0
menor = 0
quantidade = 1
while digitar_numero == 's':
        num = int(input('Digite um número: '))
        lista += [num]
        if quantidade == 1:
                menor = maior = num
                quantidade += 1
        else:
                if num > maior:
                        maior = num
                if num < menor:
                        menor = num
        continuar = str(input('Você quer continuar a digitar ? ')).strip().lower()
        if continuar == 's':
                digitar_numero = 's'
        if continuar != 's':
                dividendo = len(lista)
                lista = sum(lista)
                média = lista / dividendo
                print('a média dos números é {}, o menor é {} e o maior é {}'.format(média,menor,maior))
                exit()



#a media dos numeros, o maior e o menor