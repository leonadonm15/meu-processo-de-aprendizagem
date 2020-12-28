'''Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
e pelo menos os métodos comer(), verBucho() e digerir().
Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?'''
class Macaco:
    def __init__(self, nome, bucho=None):
        self.nome = nome
        self.bucho = bucho

    def __str__(self):
        return 'macaco dahora'

    def comer(self, comida):
        if self.bucho != None:
            print(f'{self.nome}, voce ja comeu, cague primeiro para comer novamente')
            return
        self.bucho = comida
        print(f'o macaco {self.nome} comeu {self.bucho}')

    def cagar(self):
        if self.bucho == None:
            print('voce nao tem nada no bucho, coma alguma coisa')
            return
        print(f'voce cagou {self.bucho}')
        self.bucho = None

    def ver_bucho(self):
        if self.bucho == None:
            self.bucho = 'nada'
            print(f'voce ta com {self.bucho} no bucho')
            self.bucho = None
            return
        print(f'voce ta com {self.bucho} no bucho')


macaco1 = Macaco('flavio')
macaco2 = Macaco('Adenilson')
print(macaco2)
