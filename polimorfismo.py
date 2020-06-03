class mamiferos:
    def emitir_som(self):
        pass

class cachorro(mamiferos):
    def emitir_som(self):
        print('Au au')

class gato(mamiferos):
    def emitir_som(self):
        print('Miau miau')

gato = gato()
cachorro = cachorro()
mamiferos = [gato, cachorro]

for mamifero in mamiferos:
    mamifero.emitir_som()
