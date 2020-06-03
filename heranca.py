#Codenation - Aula de Heranca

class animal:
    def fazer_barulho(self):
        print('Barulho de um animal')

#Heranca multipla
class domestico:
    def dorme_muito(self):
        return True

class mamiferos(animal):
    pass

class cachorro(mamiferos):
    pass

class gato(mamiferos,domestico):
    def fazer_barulho(self):
        print('Miau!')

#Realizando algumas instâncias
gato = gato()
gato.fazer_barulho()
print(gato.dorme_muito())

#Cachorro herda da classe 'mamiferos' que por sua vez
#herda da classe 'animal' que possui o método 'dorme_muito'
#logo a instancia a seguir vai imprimir 'Barulho de um animal'
cachorro().fazer_barulho() 

