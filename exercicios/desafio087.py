'''Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs:
Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação
entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para
armazenar esta informação por que ela pode ser calculada a qualquer momento.'''

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = None

    def __str__(self):
        print(self)

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return self.fome

    def get_saude(self):
        return self.saude

    def get_idade(self):
        return self.idade

    def change_nome(self,nome):
        self.nome = nome
        self.humor_tamagushi()
        print(f'novo nome {self.nome}')

    def change_fome(self):
        quanto_eu_quero = 100 - self.fome
        fome = int(input(f'quanto de comida que voce quer dar para o seu tamagoshi: [1-{quanto_eu_quero}] '))
        self.fome += fome
        print(f'nova fome {self.fome}')
        self.humor_tamagushi()

    def brincar(self):
        limite = self.fome / 2
        tempo = float(input(print(f'voce pode brincar por {limite} tempo')))
        self.fome = self.fome / tempo
        print('agora voce tem {:.2} de fome'.format(self.fome))
        self.humor_tamagushi()
        return self.fome

    def change_saude(self,saude):
        self.saude = saude
        self.humor_tamagushi()
        print(f'nova saude {self.saude}')

    def change_idade(self,idade):
        self.idade = idade
        self.humor_tamagushi()
        print(f'a nova idade é {self.idade}')

    def humor_tamagushi(self):
        self.humor = self.saude / self.fome
        if self.humor <= 0.4:
            print('to puto')


tamago = Tamagushi('ama', 10, 100, 1)
tamago.humor_tamagushi()
tamago.change_fome()
tamago.humor_tamagushi()
tamago.brincar()
