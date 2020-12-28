'''Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.'''

class Retangulo:
    def __init__(self, base, lado):
        self.base = base
        self.lado = lado

    def mudar_base(self, base):
        self.base = base
        print(f'a nova base tem valor de {self.base}')

    def mudar_lado(self, lado):
        self.lado = lado
        print(f'o novo lado tem valor de {self.lado}')

    def calc_area(self):
        print(self.base * self.lado)

    def calc_per(self):
        print((self.lado * 2) + (self.base * 2))

pergunta = 0
c = 0
while pergunta != 3:
    if c == 0:
        val1 = int(input('valor da base: '))
        val2 = int(input('valor do lado: '))
        ret = Retangulo(val1, val2)
        c += 1
    pergunta = int(input('1 - área\n'
                         '2 - perímetro\n'
                         '3 - sair\n'
                     '4 - mudar base\n'
                     '5 - mudar lado\n'
                     '-> '))
    if pergunta == 1:
        ret.calc_area()
    if pergunta == 2:
        ret.calc_per()
    if pergunta == 3:
        exit()
    if pergunta == 4:
        nova_base = int(input('Digite o valor na nova base: '))
        ret.mudar_base(nova_base)
    if pergunta == 5:
        novo_lado = int(input('Digite o valor no novo lado: '))
        ret.mudar_lado(novo_lado)
