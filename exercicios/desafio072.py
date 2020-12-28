def somainposto(taxaimposto, custo):
        imposto = (custo / 100) * taxaimposto
        print('a porcentagem de imposto é de {}% , o custo é de {} e o total é de {}'.format(taxaimposto, custo, custo + imposto))
t = float(input('Qual a taxa de imposto ? '))
c = float(input('Qual o preço sem o imposto? '))
somainposto(t,c)



#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem
# e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas