#Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn
# ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres
# serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
import random

def embaralhar(a):
        a = (random.sample(a, len(a)))
        a = ''.join(a)
        print('embaralhado fica -> {}'.format(a))

a = list(str(input('Digite uma palavra: ')).strip().lower())
embaralhar(a)