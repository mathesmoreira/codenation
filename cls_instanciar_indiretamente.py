#Exemplo de instancia indireta
import abc

class Pessoa(abc.ABC):
    @abc.abstractmethod
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        #self.idade = idade
        self.cpf = cpf
    
class Jovem(Pessoa):
    def __init__(self, nome, sobrenome, cpf, idade):
        super().__init__(nome, sobrenome, cpf)
        self.idade = idade
        if self.idade < 30:
            return print('Muito jovem, jovem')
        else:
            return print('Voce eh um adulto ;D')

jovem = Jovem('Matheus', 'Moreira', 1234, 17)
