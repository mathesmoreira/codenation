# Nao faz produto ter a classe Funcionario, já que todos os empregados 
# se enquadram em alguma area (secretario,gerente,direto,etc).
# Dado esse problema, usaremos classes abstratas (Abstract Base Classes, ABC)
# Uma classe abstrata nao pode ser instaciada.
# Uma classe abstrata não pode ser instanciada e deve conter pelo menos um método abstrato.
import abc

#TENTAR CADASTRAR FUNCIONARIO ATRAVES DE UMA CLASSE "CADASTRO FUNC", INSTACIA INDIRETA
class Funcionario(abc.ABC):
    @abc.abstractmethod
    def __init__(self, nome, cpf, salario):
        #Atributos privados recebem dois underline(__)
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        print('Foi instanciada!')
    #Func recebem bonificacao, padrao para todos funcioanrios
    
    def get_bonificacao(self):
        return self.salario * 0.10


#Como gerente também é um func da empresa, ele HERDA os atributos da classe 'Funcionarios'
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        #super() é usado para fazer referência a superclasse, a classe mãe
        super().__init__(nome, cpf, salario)  #Pega os atributos da classe Funcionario
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados
        #Print mostrando que self.nome foi referenciado com sucesso por super()
        #print(f'Nome do gerente: {self.nome}')
    
    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
           print("acesso negado")
           return False

    #Gerentes ganham 1.000 reais a mais de bonificacao do que um func
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

#Polimorfismo
class controleBonificacao:
    def __init__(self, total_bonificacoes = 0):
        self.__total_bonificacoes = total_bonificacoes
    
    #Variável 'funcionario' guarda uma referencia ao obj Funcionario
    def registra(self, obj):
        #Funcao hasattr para verificar sem o obj tem o atributo 'get_bon..'
        if(hasattr(obj,'get_bonificacao')):
            self.__total_bonificacoes += funcionario.get_bonificacao()
        else:
            print(f'Instancia de {self.__class__.__name__} nao verificada') 

    @property
    def total_bonificacoes(self):
        return self.__total_bonificacoes
# A criacao da classe 'controleBonificacao' poderá ser aplicada para futuras classes criadas
# Exemplo: Secretaria, Cantina...., evitando a implementacao repetida desse metodo

#Funcionario('Matheus', '33333-3', 2000.0)
gerente = Gerente('José', '222222222-22', 5000.0, '1234', 0)

# controle = controleBonificacao()
# controle.registra(funcionario)
# controle.registra(gerente)
##Esse print imprime a localizacao do objeto
#print(gerente.get_bonificacao)
##Esse print retorna o valor da bonificacao
#print(gerente.get_bonificacao()) 
##Use vars() para acessar os atributos de gerente
#print(vars(gerente)) 

class Cliente:
    def __init__(self, nome, cpf, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
#Tentando registrar um nao funcionário
# cliente = Cliente('Josefino', 12344, 4111)
# controle = controleBonificacao()
# controle.registra(cliente)
# Ao tentar registrar cliente aparecerá um erro, pois cliente nao tem get_bonificacao

#Verificando que toda classe é filha da classe Objeto
class MinhaClasse():
    pass

if __name__ == '__main__':
    mc = MinhaClasse()
    #Métodos mágicos da classe
    #print(dir(mc)) #Todos esses atributos herdados da classe Objeto

# print(mc)
# Funcao print usa um metodo _str_() de uma classe
# Vamos reescrever esse método 
class MinhaClasse:
    def __str__(self):
        return '<Instancia de: {};  endereco: {}>'.format(self.__class__.__name__, id(self))
mc = MinhaClasse()
# print(mc)

