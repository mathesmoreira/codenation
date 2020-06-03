#nome = input('Digite o nome: ')

class cliente:    
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        return print(nome, preco)

class carrinho_valor:
    def __init__(self, cliente, produtos):
        self.cliente = cliente
        self.produtos = produtos
        #print(cliente)
    
    @property    
    def total_valor(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco
        return total

    def imprimindo(self):
        print(f'O valor total é {self.total_valor}')

cliente = cliente('Matheus','123')
tv = produto('TV', 100)
pc = produto('PC', 1000)
produtos = [tv,pc]
carrinho = carrinho_valor(cliente, produtos)
print(carrinho.imprimindo())
#print(carrinho)
