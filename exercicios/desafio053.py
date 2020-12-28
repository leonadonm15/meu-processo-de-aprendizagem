fr = ''.join(str(input('Escreva uma frase e direi se é um palindromo ')).split())
infr = fr[::-1]

if fr == infr:
    print('essa frase é um plindromo')
else:
    print('Essa frase nao é um palindromo')

