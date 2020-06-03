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


gato = gato()
gato.fazer_barulho()
cachorro().fazer_barulho()

print(gato.dorme_muito())