'''Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:'''

class Carro:
    def __init__(self, autonomia):
        self.autonomia = float(autonomia)
        self.kilomatragem = None
        self.gasolina = None

    def andar(self):
        if self.gasolina != 0:
            self.kilomatragem = self.gasolina / self.autonomia
            print(f'voce andou {self.kilomatragem} kilometros com {self.gasolina} de gasolina')
            self.gasolina = 0
        else:
            print(f'seu {self} esta sem gasolina, abasteça')

    def ober_gasolina(self):
        print(f'voce tem {self.gasolina}L de gasolina')

    def adicionar_gasolina(self, gasolina):
        self.gasolina = gasolina
        print(f'voce colocou {self.gasolina} de gasolina')

corsa = Carro(11.4)
corsa.adicionar_gasolina(114)
corsa.andar()
corsa.ober_gasolina()
