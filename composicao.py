class cliente:
    def __init__(self,nome,documento):
        self.nome = nome
        self.documento = documento

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class carrinho_compra:
    def __init__(self,cliente,produtos):
        self.num_pedido = '123'
        self.produtos = produtos
        self.cliente = cliente
        #print(cliente)
    @property #Acessar funcao como fosse um atributo
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco

        return total
    
    def add_produto(self, produto):
        self.produto.append(produto)

    def remove_produto(self, produto):
        self.produto.remove(produto)

    def fechar_carrinho(self):
        print(f'Fechando o pedido: {self.num_pedido}')
        print(f'Valor da compra: {self.valor_carrinho}')
        print(f'Nome cliente: {self.cliente.nome}')

cliente = cliente('Matheus','1234')

televisao = produto('televisao', 1000.09)
maq_cafe = produto('maquina de café', 399.90)

produto = [televisao,maq_cafe]

carrinho = carrinho_compra(cliente,produto)

#print(carrinho.fechar_carrinho())