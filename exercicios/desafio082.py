'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, cor):
        self.cor = cor

    def mostrar_cor(self):
        print(f'a cor da bola é {self.cor}')

bola1 = Bola('amarelo', 10, 'cilicone')
bola1.mostrar_cor()

bola1.trocar_cor('vermelho')
bola1.mostrar_cor()
