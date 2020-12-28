'''Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = float(peso)
        self.altura = float(altura)
        self.aniversario = 0

    def crescer(self, altura):
        self.altura += altura
        print(f'você cresceu {altura} de altura, tendo agora {self.altura}')

    def evelhecer(self):
        self.aniversario += 1
        if self.idade < 21:
            self.altura += 0.05
            print(f'voce cresceu 0.05 de altura, tendo agora {self.altura}')
        if self.idade >= 21:
            print('voce ta velho ja pra crescer')
        print(f'Você agora tem {self.idade} anos')

    def engordar(self):
        self.peso += 10
        print(f'voce engordou 10 kilos, agora ta com {self.peso}')

    def emagrecer(self):
        self.peso -= 5
        print(f'voce emagreceu 5 kilos, agora ta com {self.peso}')

leonardo = Pessoa('leonardo', 16, 80, 1.74)
