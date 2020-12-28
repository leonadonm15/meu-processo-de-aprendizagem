maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('Qual o seu peso? '))
    if c == 1:
        menor = maior
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('''a pessoa com mais peso tem {}KG e a pessoa com menos kilos tem {}KG'''.format(maior,menor))
