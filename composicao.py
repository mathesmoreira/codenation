#Aula AceleraDev, Python
#COMPOSICAO

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

    @property #Para acessar funcao como fosse um atributo
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco
        return total

    def add_produto(self, produto):
        self.produtos.append(produto)

    def remove_produto(self, produto):
        self.produtos.remove(produto)

    def fechar_carrinho(self):
        print(f'Fechando o pedido: {self.num_pedido}')
        print(f'Valor da compra: {self.valor_carrinho}')
        print(f'Nome cliente: {self.cliente.nome}')


#Testando as classes
#Informando cliente e produtos
cliente = cliente('Matheus','1234')
televisao = produto('televisao', 1000.09)
maq_cafe = produto('maquina de café', 399.90)
celular = produto('celular',400.00)

produto = [televisao,maq_cafe,celular]
carrinho = carrinho_compra(cliente,produto)
#Adicionando um produto novo ao carrinho
choveiro = produto('choveiro', 250.0)
carrinho.add_produto(choveiro)
carrinho.fechar_carrinho()

