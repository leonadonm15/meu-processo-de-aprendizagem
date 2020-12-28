nome_nota = {}
nome = nome_nota['nome'] = [input('qual o seu nome: ')] # a var nome é a lista dentro do dicionario que contem os valores dos nomes
nome_nota['nota'] = [input('qual foi a sua nota: ')]

if nome_nota['nota'] == ['']:
    nome_nota['nota'] = 0

nome.append('Juão') #usa o metodo append ao enves de += juao pra nao separar os caracteres dentro da lista

#nome_nota.update({'nome':(nota,'Juão')})

print(nome_nota['nome'][1])

def adicionar_nome(nome):
    nome.append(nome)

'''
scriptzinho util pra armazenamento de dados de diversos tipos
quebra galho pra nao precisar usar sql tao cedo
'''