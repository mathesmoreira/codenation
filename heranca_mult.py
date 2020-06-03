class Cao:
    qt_patas = 4
    carnivoro = True
    nervoso = False

    def __init__(self,nome):
        self.nome = nome
    
    def latir(self, vezes = 1):
        #Quando nervoso, late o dorbro
        vezes = vezes + (self.nervoso*vezes)
        print(f'{self.nome} :'+ ' Au'*vezes)
    def __str__(self):
        return self.nome




    



# cao = Cao('Yoshi')
# grande = cao.latir(2)
# #cao.latir(2)
