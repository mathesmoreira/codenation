import datetime

class Conta:
#'limite' recebe um valor padrao, onde não é necessário informa-lo cada vez que chama o objeto
#Conta recebe o valor da classe Cliente ( cliente = Cliente(...)) 
    def __init__(self, numero, cliente, saldo, limite = 1000): 
       self.numero = numero
       self.titular = cliente
       self.saldo = saldo
       #Evitando de instanciar Historico cada vez que instanciar Conta
       self.historico = Historico()

       print(f'{self.numero}, {self.titular}, {self.saldo}, {limite}')
    
    def extrato(self):
        print(f'Número: {self.numero} \nSaldo: {self.saldo}')
        self.historico.transacoes.append(f'Tirou o extrato - saldo: {self.saldo}')

    def deposita(self, saldo):
        self.saldo += saldo
        print(f' Foi depositado {saldo} reais. O seu saldo novo é de {self.saldo} reais')
        self.historico.transacoes.append(self.saldo)

    def saca(self, saca):
        self.saldo -= saca
        if self.saldo < 0:
            print('Voce nao tem dinheiro o suficiente para sacar')
            return False
        else:
            print(f'Foi sacado {saca} reais. Seu saldo atual é de {self.saldo} reais')
            self.historico.transacoes.append(self.saldo)

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'Transferencia no valor de {valor} para {destino}')
            return True


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

#Historico compõe a classe Conta
class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'Data de abertura: {self.data_abertura}')
        print('Transacões: ')
        for t in self.transacoes:
            print('-', t)

