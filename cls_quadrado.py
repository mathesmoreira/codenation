#Criando uma classe que calcula a área de um quadrado
class Quadrado:

    def __init__(self, t = 0):
        self.tamanho_lado = t

    def mudar_valor_lado(self, novo_valor):
        self.tamanho_lado = novo_valor
        return print(f'O novo valor do lado é {self.tamanho_lado}')

    def calculo_area(self):
        self.calculo_area = self.tamanho_lado**2
        return print(f'O valor da área do quadrado é {self.calculo_area}')

#Realizando alguns testes
quadrado = Quadrado(3)
quadrado.mudar_valor_lado(4)
quadrado.calculo_area()